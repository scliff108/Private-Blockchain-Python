"""
Application Server
(Do not change this code)
This is how you will run and test your private blockchain.
To start your server, navigate to the folder containing this document in a terminal window.
Type the command: py api.py
Your program will start. Follow the URL in the Terminal.
app.route shows the different pages you can navigate to.
There is a home page that lists the hash values of the blocks in the chain.
There is a page to get a block by it's height (/block/height)
There is a page to submit a star (/submit_star)
There is a page to get a block by it's hash (/block/hash)
"""

import flask
from flask import request, jsonify
from src.blockchain import blockchain as blockchain_class
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Initialize Blockchain
blockchain = blockchain_class()

# Home Page that lists Blocks in Blockchain
@app.route('/', methods=['GET'])
def home():
    blocks = '<ol>'
    for block in blockchain.chain:
        blocks += '<li>' + block.hash + '</li>'
    blocks += '</ol>'
    return blocks

# Endpoint to Get a Block by Height (GET Endpoint)
# Go to URL/block/height?height={height} to return the block at the specified height
@app.route('/block/height', methods=['GET'])
def api_block_height():
    if 'height' in request.args:
        height = int(request.args['height'])
        for block in blockchain.chain:
            if block.height == height:
                return str(block.get_block_data())
    else:
        return "Error. No height field provided. Please specify a height."

# Endpoint that allows you to submit a star.
# Go to URL/submit_star?address={address}&star={star} to add a star to the chain
@app.route('/submit_star', methods=['GET', 'POST'])
def api_submit_star():
    if 'address' in request.args and 'star' in request.args:
        address = request.args['address']
        star = request.args['star']

        block = blockchain.submit_star(address, star)
        if block:
            return block.hash
        else:
            return "Error. Something went wrong when submitting your star."
    else:
        return "Error. Check your Body Parameter."
    
# This endpoint allows you to retrieve the block by hash (GET endpoint)
# Go to URL/block/hash?hash={hash} to return the block with the specified hash value
@app.route('/block/hash', methods=['GET'])
def api_get_block_by_hash():
    if 'hash' in request.args:
        hash = request.args['hash']
        return blockchain.get_block_by_hash(hash)
    else:
        return "Error. No hash field provided."

app.run()