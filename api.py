import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data
test_data = [
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

# A route to return all of the test data
@app.route('/block/height', methods=['GET'])
def api_block_height():
    if 'height' in request.args:
        height = int(request.args['height'])
    else:
        return "Error. No height field privided. Please specify a height."
    

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
    
    return jsonify([data for data in test_data if data['id'] == id])

app.run()