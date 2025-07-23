from solana.rpc.api import Client

def check_balance(address):
    solana_client = Client("https://api.mainnet-beta.solana.com")
    balance = solana_client.get_balance(address)
    return balance['result']['value']
