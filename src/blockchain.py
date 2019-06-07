"""
The Blockchain class contains the basic functions to create your own private
blockchain. It uses 'hashlib' to create the hashes for each block and
______________ to verify a message signature. The chain is stored in a list.
Of course each time you run the application the chain will be empty because 
a list is not a persistent storage method.
"""
import src.block as block_class
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

    def request_message_ownership_verification(self, address):
        return address + ':' + str(int(time.time())) + ':star_registry'

    def submit_star(self, address, message, signature, star):
        star_time = int(message.split(':')[1])
        current_time = int(time.time())
        if star_time > current_time - 300000:
            return self.add_block(block_class.block({'owner':address, 'star':star}))
            # TODO verify message with signature
            """
            if message verified:
                self.add_block(block_class.block({'owner': address, 'star':star}))
            else:
                return "Error. Block message was not verified."
            """
        else:
            return "Error. Block was not added due to timeout."
    
    def get_block_by_hash(self, hash):
        for block in self.chain:
            if block.hash == hash:
                return block.get_block_data()
        return "Block not in chain."
        # return block if it has the hash value
