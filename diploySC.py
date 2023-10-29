import json

from web3 import Web3

# Fill in your infura API key here
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount=web3.eth.accounts[0]
abi=json.loads('[{"inputs":[],"name":"Greeter1st","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
bytecode="608060405234801561001057600080fd5b506105c2806100206000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c8063a413686214610051578063bdcba1841461006d578063cfae321714610077578063ef690cc014610095575b600080fd5b61006b6004803603810190610066919061034e565b6100b3565b005b6100756100cd565b005b61007f61011b565b60405161008c91906103d0565b60405180910390f35b61009d6101ad565b6040516100aa91906103d0565b60405180910390f35b80600090805190602001906100c992919061023b565b5050565b6040518060400160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061011892919061023b565b50565b60606000805461012a906104a6565b80601f0160208091040260200160405190810160405280929190818152602001828054610156906104a6565b80156101a35780601f10610178576101008083540402835291602001916101a3565b820191906000526020600020905b81548152906001019060200180831161018657829003601f168201915b5050505050905090565b600080546101ba906104a6565b80601f01602080910402602001604051908101604052809291908181526020018280546101e6906104a6565b80156102335780601f1061020857610100808354040283529160200191610233565b820191906000526020600020905b81548152906001019060200180831161021657829003601f168201915b505050505081565b828054610247906104a6565b90600052602060002090601f01602090048101928261026957600085556102b0565b82601f1061028257805160ff19168380011785556102b0565b828001600101855582156102b0579182015b828111156102af578251825591602001919060010190610294565b5b5090506102bd91906102c1565b5090565b5b808211156102da5760008160009055506001016102c2565b5090565b60006102f16102ec84610417565b6103f2565b90508281526020810184848401111561030d5761030c61056c565b5b610318848285610464565b509392505050565b600082601f83011261033557610334610567565b5b81356103458482602086016102de565b91505092915050565b60006020828403121561036457610363610576565b5b600082013567ffffffffffffffff81111561038257610381610571565b5b61038e84828501610320565b91505092915050565b60006103a282610448565b6103ac8185610453565b93506103bc818560208601610473565b6103c58161057b565b840191505092915050565b600060208201905081810360008301526103ea8184610397565b905092915050565b60006103fc61040d565b905061040882826104d8565b919050565b6000604051905090565b600067ffffffffffffffff82111561043257610431610538565b5b61043b8261057b565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b82818337600083830152505050565b60005b83811015610491578082015181840152602081019050610476565b838111156104a0576000848401525b50505050565b600060028204905060018216806104be57607f821691505b602082108114156104d2576104d1610509565b5b50919050565b6104e18261057b565b810181811067ffffffffffffffff82111715610500576104ff610538565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f830116905091905056fea2646970667358221220b670d51a14c5aab47b6d9bbf26115560d4b0cb3a30f13783233ca7f1a8907eaf64736f6c63430008070033"
Greeter=web3.eth.contract(abi=abi,bytecode=bytecode)

tx_hash = Greeter.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(web3.toHex(tx_hash))

"""contract=web3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
print(contract.functions.greet().call())"""

contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi,
)

print(tx_receipt.contractAddress)

tx_hash=contract.functions.setGreeting('hi_rezvi').transact()
web3.eth.wait_for_transaction_receipt(tx_hash)
print(contract.functions.greet().call())

print('Default contract greeting: {}'.format(
    contract.functions.greet().call()
))