import json

from web3 import Web3

# Fill in your infura API key here
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

web3.eth.defaultAccount=web3.eth.accounts[0]

address=web3.toChecksumAddress("0x63933fcb7a6d671fA7859324e6185410586b4aa6")
abi=json.loads('[{"inputs":[],"name":"Greeter1st","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

contract=web3.eth.contract(address=address,abi=abi)
print(contract.functions.greet().call())
tx_hash=contract.functions.setGreeting('hi_rezvi').transact()
web3.eth.wait_for_transaction_receipt(tx_hash)
print(contract.functions.greet().call())

tx_hash=contract.functions.Greeter1st().transact()
web3.eth.wait_for_transaction_receipt(tx_hash)
print(contract.functions.greet().call())