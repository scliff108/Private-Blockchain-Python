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

    """
    Constructor of the class, you will need to setup your chain list 
    and the height of your chain.
    Everytime you create a Blockchain class you will need to initialize
    the chain creating the Genesis Block.
    """
    def __init__(self):
        self.chain = []
        self.height = -1
        self.initialize_chain()

    """
    This method will check for the height of the chain and if there isn't 
    a Genesis Block it will create it.
    You should use the add_block(block) to create the Genesis Block passing
    {'data': 'Genesis Block'} as data
    """
    def initialize_chain(self):
        if self.height is -1:
            block = block_class.block({'data': 'Genesis Block'})
            self.add_block(block)
    
    """
    add_block(block) will store a block in the chain
    The method will return a block if the block was added correctly
    or it will return an error message that the block was not added.
    1. Timestamp the block with the time it was created.
    2. Assign the block a previous block hash unless it is the Genesis Block
    3. Set the block height
    4. Set the hash of the block
    5. Append the block to the chain
    6. Increment the chain height.
    Use this line of code to calculate the block hash:
    sha256(json.dumps(block.__dict__).encode()).hexdigest()
    """
    def add_block(self, block):
        return True # TEMP RETURN VALUE

    """
    submit_star(address, star) will allow users to register a new block with the 
    star object in the chain. This method will return the block added to the chain.
    1. Create a new block with the address and star
    2. Return the block
    """
    def submit_star(self, address, star):
        return True # TEMP RETURN VALUE
    

    """
    get_block_by_hash(hash) will return a block with a given hash value or an error
    stating the block is not in the chain.
    1. Check if the hash value represents a block in the chain.
    2. Return the block or the error message.
    """
    def get_block_by_hash(self, hash):
        return True # TEMP RETURN VALUE