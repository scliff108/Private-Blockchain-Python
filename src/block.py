"""
The Block class is a main component into any Blockchain Platform, it will
store the data and act as a dataset for your application. The class will
expose a method to validate the data... The body of the block will contain an
Object that contains the data to be stored, the data should be stored encoded.
"""
from hashlib import sha256
import json
import binascii

class block:

    def __init__(self, data):
        self.hash = None                                            # Hash of the block
        self.height = 1                                             # Block Height (consecutive number of each block)
        self.body = str(binascii.hexlify((json.dumps(data).encode())))[2:-1]   # Contains the encoded transactions in the block
        self.time = 0                                               # Timestamp for the Block creation
        self.previousBlockHash = None                               # Reference to the previous Block Hash
    
    """
    Function to make sure the block has not been tampered with.
    If the data inside the block has been tampered with then the hash value
    will be different than the hash of the block.
    1. Return True if the block is valid.
    2. Return False if the block has been tampered with.
    Use this line of code to calculate the hash value:
    sha256(json.dumps(temp_block.__dict__).encode()).hexdigest()
    """
    def validate(self):
        return True # TEMP RETURN VALUE

    """
    Return the decoded body of the block.
    1. If the block is the genesis block, simply return "This is the Genesis Block"
    2. Decode the data in the block body.
    3. If there is data in the body, return it
    4. If there is no data in the body, return with an error message.
    Use this line of code to decode the data_object:
    json.loads(bytes.fromhex(encoded_data).decode('ascii'))
    """
    def get_block_data(self):
        return True # TEMP RETURN VALUE