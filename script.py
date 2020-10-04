import json
from flask import Flask
from serve import useless_function  

app=Flask(__name__)

# Define our "ping" end point
@app.route('/ping')
def useless_output():
  return(useless_function())

# load our pre-trained model & function
classifier_api = get_classifier_api()

# Define a post method for our API.
@app.route('/classify', methods=['POST'])
def classify():
    """ 
    Takes in a json file, extracts the keywords &
    their indices and then returns them as a json file.
    """
    # the data the user input, in json format
    input_data = request.json

    # use our API function to get the keywords
    output_data = classifier_api(input_data)

    # convert our dictionary into a .json file
    # (returning a dictionary wouldn't be very
    # helpful for someone querying our API from
    # java; JSON is more flexible/portable)
    response = json.dumps(output_data)

    # return our json file
    return response
