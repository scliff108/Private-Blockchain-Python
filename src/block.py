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
    
    def validate(self):
        temp_block = self
        temp_block.hash = None
        calculated_hash = sha256(json.dumps(temp_block.__dict__).encode())
        if calculated_hash is self.hash:
            return True
        return False

    def get_block_data(self):
        if self.height is 0:
            return "This is the Genesis Block"
        encoded_data = self.body
        data_object = json.loads(bytes.fromhex(encoded_data).decode('ascii'))

        if data_object:
            return data_object
        else:
            return "Error decoding the data object"
