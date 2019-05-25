"""
The Blockchain class contains the basic functions to create your own private
blockchain. It uses 'hashlib' to create the hashes for each block and
______________ to verify a message signature. The chain is stored in a list.
Of course each time you run the application the chain will be empty because 
a list is not a persistent storage method.
"""
import block as block_class
from hashlib import sha256
import json
import time

class blockchain:

    def __init__(self):
        self.chain = []
        self.height = -1
        self.initialize_chain()

    def initialize_chain(self):
        if self.height is -1:
            block = block_class.block({'data': 'Genesis Block'})
            self.add_block(block)
        
    def add_block(self, block):
        block.height = self.height + 1
        block.time = int(time.time())
        if len(self.chain) > 0:
            block.previousBlockHash = self.chain[self.height].hash
        block.hash = sha256(json.dumps(block.__dict__).encode()).hexdigest()
        self.chain.append(block)
        self.height += 1

        if self.chain[self.height] is block:
            return block
        return "Error. Block was not added"
