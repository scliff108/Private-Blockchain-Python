import flask
from flask import request, jsonify
from src.blockchain import blockchain as blockchain
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data
blocks = [
    {
        'height': 0,
        'body': 'Test Genesis Block',
        'time': 't'
    },
    {
        'height': 1,
        'body': 'Test 1st Block',
        'time': 't+1'
    },
    {
        'height': 2,
        'body': 'Test Second Block',
        'time': 't+2'
    }
]

@app.route('/', methods=['GET'])
def home():
    return '<h1>WELCOME</h1>'

# Endpoint to Get a Block by Height (GET Endpoint)
@app.route('/block/height', methods=['GET'])
def api_block_height():
    if 'height' in request.args:
        height = int(request.args['height'])
    else:
        return "Error. No height field provided. Please specify a height."
    return jsonify([block for block in blocks if block['height'] == height])

# Endpoint that allows user to request Ownership of a Wallet address (POST Endpoint)
@app.route('/request_validation', methods=['GET', 'POST'])
def api_request_validation():
    print("Running api request validation")
    if 'address' in request.args:
        address = request.args['address']
        message = blockchain().request_message_ownership_verification(address) # TODO: Create request_message_ownership_verification(address) function
        if message:
            return message
        else:
            return "Error. There was an error in creating your message."
    else:
        return "Error. No address field provided. Please specify an address."

# Get a specific piece of data by ID
@app.route('/api/v1/resources/test_data', methods=['GET'])
def api_id():
    """
    Check if an ID was provided
    If it was, assign it to a variable
    If not, display an error
    """
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error. No id field provided. Please specify an id."
    
    return jsonify([block for block in blocks if block['id'] == id])

app.run()