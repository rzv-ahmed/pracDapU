import json

from web3 import Web3

# Fill in your infura API key here
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

acc1="0x34fDE2aDc97ba23E2418a3e02DAE14799C78A953"
acc2="0x8A181B1d20d264B8A8a28b210FEcCef5f270f35E"
private_key="0x6d239340c515a759b7cb2c00efb4a5751245e01e8390d087c8f18a139dbe79da"


#get a nonce
nonce =web3.eth.getTransactionCount(acc1)

#build a transaction
tx={
    'nonce': nonce,
    'to':acc2 ,
    'value': web3.toWei(5,'ether'),
    'gas': 2000000,
    'gasPrice':web3.toWei('70','gwei')

}
#sign transaction
signed_tx=web3.eth.account.signTransaction(tx,private_key)
#send transaction
tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# wait for the transaction
transaction_receipt=web3.eth.wait_for_transaction_receipt(tx_hash)
print( )