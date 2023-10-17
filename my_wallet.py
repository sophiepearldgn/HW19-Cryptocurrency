 from eth_account import Account

def create_wallet():
    wallet = Account.create()
    return wallet

def derive_account(wallet, index):
    derived_account = wallet.derive(f"m/44'/60'/0'/0/{index}")
    return derived_account
from web3 import Web3

def get_balance(address, infura_url):
    w3 = Web3(Web3.HTTPProvider(infura_url))
    balance_wei = w3.eth.getBalance(address)
    return w3.fromWei(balance_wei, 'ether')

# estimate gas
def estimate_gas(sender, to, value, data, infura_url):
    w3 = Web3(Web3.HTTPProvider(infura_url))
    gas_estimate = w3.eth.estimateGas({
        'from': sender,
        'to': to,
        'value': value,
        'data': data,
    })
    return gas_estimate

# send raw transaction
def send_raw_transaction(sender, private_key, to, value, data, infura_url):
    w3 = Web3(Web3.HTTPProvider(infura_url))
    nonce = w3.eth.getTransactionCount(sender)
    
    transaction = {
        'to': to,
        'value': value,
        'gas': 21000,  # Adjust this based on gas estimation
        'gasPrice': w3.toWei('20', 'gwei'),  # Set an appropriate gas price
        'nonce': nonce,
    }
    
    
    signed_transaction = w3.eth.account.signTransaction(transaction, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return tx_hash.hex()


----------------------------------------

from eth_account import Account

# Generate a new Ethereum account
account = Account.create()

# Retrieve the mnemonic seed phrase
mnemonic_seed = account._address._mnemonic