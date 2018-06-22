blockchain = []

def addValue(value, lastTransaction=[1]):
    blockchain.append([lastTransaction, value])
    return blockchain

def getLastBlockchainValue():
    return blockchain[-1]

def askForTransaction(times=1):
    for i in range(times):
        tx_amount = float(input("Your transaction amount: "))
        if len(blockchain) == 0:
            addValue(tx_amount)
        else:
            addValue(tx_amount, getLastBlockchainValue())

askForTransaction(3)
print(blockchain)