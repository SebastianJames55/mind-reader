import logging

from flask import Flask, jsonify, g, Blueprint
from flask_restx import Api, Resource

import config
import constants
from connectors import MindsDBConnector
from models import MindsDBModel

app = Flask(__name__)
# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Create a logger for your module
logger = logging.getLogger(__name__)


# Function to get the connector based on the specified app in config.py
def get_connector():
    # Create a connector based on the specified app in config.py
    if config.APP_TO_CONNECT == constants.MINDSDB:
        logger.debug('Choosing mindsdb app')
        return MindsDBConnector()
    else:
        raise ValueError(constants.INVALID_APP_MESSAGE)


# Function to get the model based on the specified app in config.py
def get_model():
    if config.APP_TO_CONNECT == constants.MINDSDB:
        return MindsDBModel()
    else:
        raise ValueError(constants.INVALID_APP_MESSAGE)


@app.before_request
def before_request():
    # Set the connector and model instances as application context variables
    g.connector = get_connector()
    g.model = get_model()


# Create a versioned API Blueprint
api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Initialize Flask-RESTPlus Api object
api = Api(api_v1, version='1.0', title='Mind Reader API', description='API for the Mind Reader backend')

# Define a namespace for the API
ns = api.namespace('predict', description='Prediction operations')


@ns.route('/')
class Predict(Resource):
    @api.doc('predict')
    def post(self):
        """
        Make a prediction
        """
        try:
            # Data to predict
            data = "why is gravity so different on the sun?"

            # Make predictions using the connector and model
            prediction = g.connector.predict(data)

            return jsonify(prediction)

        except Exception as e:
            # Graceful error handling
            error_message = f"An error occurred: {str(e)}"
            return jsonify({'error': error_message}), 500


# Register the API Blueprint
app.register_blueprint(api_v1)

if __name__ == '__main__':
    app.run(debug=True)
