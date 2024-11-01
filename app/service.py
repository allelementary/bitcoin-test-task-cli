import requests
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from bitcoin.core import b2lx, x
from bitcoin.core.script import CScript
from bitcoin.core import CTransaction

from app.models import Transaction


def create_wallet():
    try:
        key = PrivateKeyTestnet()
        return key.address, key.to_wif()
    except Exception as e:
        print(f"Error creating wallet: {e}")


def get_block_height():
    try:
        response = requests.get("https://blockstream.info/testnet/api/blocks/tip/height")
        response.raise_for_status()
        block_height = response.text
        return block_height
    except requests.exceptions.RequestException as e:
        print(f"Error fetching block height: {e}")


def send_transaction(private_key_wif, recipient, amount):
    try:
        key = PrivateKeyTestnet(private_key_wif)
        utxos = key.get_unspents()
        print(f"UTXOS: {utxos}")
        raw_tx = key.create_transaction([(recipient, amount, 'satoshi')], fee=5)

        url = "https://blockstream.info/testnet/api/tx"
        headers = {'Content-Type': 'text/plain'}
        response = requests.post(url, data=raw_tx, headers=headers)

        if response.status_code == 200:
            print(f"Transaction sent successfully! TXID: {response.text}")
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

        return response.text

    except Exception as e:
        print(f"Error sending transaction: {e}")
        raise e


def save_tx(txid):
    tx_info = get_tx_details(txid)
    Transaction.save_transaction_to_db(tx_info)


def get_tx_details(txid):
    try:
        raw_tx_hex = NetworkAPI.get_transaction_by_id_testnet(txid)
        raw_tx_bytes = x(raw_tx_hex)
        tx = CTransaction.deserialize(raw_tx_bytes)

        tx_id = b2lx(tx.GetTxid())
        inputs = [
            {"txid": b2lx(vin.prevout.hash), "vout": vin.prevout.n}
            for vin in tx.vin
        ]
        outputs = [
            {
                "address": str(CScript(vout.scriptPubKey)),
                "value": vout.nValue
            }
            for vout in tx.vout
        ]
        total_input_value = sum(inp.get("value", 0) for inp in inputs)
        total_output_value = sum(out["value"] for out in outputs)
        amount = total_input_value - total_output_value

        return {
            "tx_id": tx_id,
            "inputs": inputs,
            "outputs": outputs,
            "amount": amount,
        }

    except Exception as e:
        print(f"Error fetching or decoding transaction details: {e}")
        return None
