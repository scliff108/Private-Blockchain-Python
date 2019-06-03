import flask
from flask import request, jsonify
from src.blockchain import blockchain as blockchain_class
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Initialize Blockchain
blockchain = blockchain_class()

@app.route('/', methods=['GET'])
def home():
    blocks = '<ol>'
    for block in blockchain.chain:
        blocks += '<li>' + block.hash + '</li>'
    blocks += '</ol>'
    return blocks

# Endpoint to Get a Block by Height (GET Endpoint)
@app.route('/block/height', methods=['GET'])
def api_block_height():
    if 'height' in request.args:
        height = int(request.args['height'])
        for block in blockchain.chain:
            if block.height == height:
                return str(block.get_block_data())
    else:
        return "Error. No height field provided. Please specify a height."

# Endpoint that allows you to submit a star. Must request ownership before submitting star.
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
@app.route('/block/hash', methods=['GET'])
def api_get_block_by_hash():
    if 'hash' in request.args:
        hash = request.args['hash']
        return blockchain.get_block_by_hash(hash)
    else:
        return "Error. No hash field provided."

app.run()