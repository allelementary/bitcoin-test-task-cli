import argparse

from app.service import get_block_height, create_wallet, send_transaction, get_tx_details, save_tx


async def main():
    parser = argparse.ArgumentParser(description="Test task CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("createwallet", help="Create new wallet")

    subparsers.add_parser("getblockheight", help="Get the current block height")

    info = subparsers.add_parser("txinfo", help="Get tx info")
    info.add_argument("tx_hash", help="tx hash")

    save = subparsers.add_parser("savetx", help="Save tx details to db")
    save.add_argument("tx_id", help="tx id")

    create_tx_parser = subparsers.add_parser("createtx", help="Create a new transaction")
    create_tx_parser.add_argument("recipient", help="Recipient address")
    create_tx_parser.add_argument("amount", type=int, help="Amount to send")
    create_tx_parser.add_argument("private_key_wif", help="Sender private key WIF")

    args = parser.parse_args()

    if args.command == "getblockheight":
        block_height = get_block_height()
        print(f"Block Height: {block_height}")
    elif args.command == "createtx":
        txid = send_transaction(
            private_key_wif=args.private_key_wif,
            recipient=args.recipient,
            amount=args.amount,
        )
        print(f"Created Transaction ID: {txid}")
    elif args.command == "createwallet":
        address, key = create_wallet()
        print(f"Wallet address: {address} | Key: {key}")
    elif args.command == "txinfo":
        tx_info = get_tx_details(args.tx_hash)
        print(f"Transaction info: {tx_info}")
    elif args.command == "savetx":
        save_tx(args.tx_id)
        print("Transaction saved to db")


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
