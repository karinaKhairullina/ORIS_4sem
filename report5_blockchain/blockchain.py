from hashlib import sha256
from time import time

class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.prevHash = None
        self.nonce = 0
        self.hash = self.getHash()

    def getHash(self):
        hash = sha256()
        hash.update(str(self.prevHash).encode('utf-8'))
        hash.update(str(self.timestamp).encode('utf-8'))
        hash.update(str(self.data).encode('utf-8'))
        hash.update(str(self.nonce).encode('utf-8'))
        return hash.hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.getHash()

class Blockchain:

    def __init__(self):
        self.chain = [Block(str(int(time())))]
        self.difficulty = 4
        self.blockTime = 20

    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, block):
        block.prevHash = self.getLastBlock().hash
        block.hash = block.getHash()
        block.mine(self.difficulty)
        self.chain.append(block)


if __name__ == '__main__':
    blockchain = Blockchain()

    for i in range(5):
        block = Block()
        blockchain.addBlock(block)

    for block in blockchain.chain:
        print(f'Когда был создан блок: {block.timestamp}')
        print(f'Данные блока: {block.data}')
        print(f'Предыдущий хеш: {block.prevHash}')
        print(f'Nonce: {block.nonce}')
        print(f'Текущий хеш: {block.hash}')
        print('----------------------')


