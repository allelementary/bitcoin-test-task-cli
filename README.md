# Bitcoin Test Task CLI

Test Task for Python Blockchain Developer Position

## About

This project is a Python-based Bitcoin CLI application designed to interact with the Bitcoin Testnet. It provides functionalities to:

- Create wallets and manage private keys
- Fetch blockchain data (e.g., block height)
- Create and send transactions
- Retrieve transaction details
- Save transaction data to a PostgreSQL database
- The application uses Blockstream's API to interact with the Bitcoin Testnet.

## Usage
1. Prerequisites
   - Python 3.12+

   - Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

   - Create `.env` file and add database credentials
   - Run Alembic Migration:
   ```bash
   alembic upgrade head
   ```

2. Available Commands
   - Create a New Wallet
   Generates a new Bitcoin Testnet wallet with an address and private key (WIF)
   ```bash
   python main.py createwallet
   ```

   - Get the Current Block Height
   Fetch the latest block height from the Bitcoin Testnet
   ```bash
   python main.py getblockheight
   ```

   - Create a New Transaction
   Create and broadcast a transaction on the Bitcoin Testnet
   ```bash
   python main.py createtx <recipient_address> <amount_in_satoshis> <private_key_wif>
   ```

   - Get Transaction Info
   Retrieve detailed information for a given transaction
   ```bash
   python main.py txinfo <tx_hash>
   ```
   
   - Save Transaction to Database
   Save the transaction details to the PostgreSQL database
   ```bash
   python main.py savetx <tx_id>
   ```
   
3. Get Testnet Coins (Faucet)
   Use the following Bitcoin Testnet faucet to get test coins:
   `https://coinfaucet.eu/en/btc-testnet/`
