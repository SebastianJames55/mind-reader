import logging

from flask import Flask, g, Blueprint
from flask_restx import Api

import config
import constants
from connectors import MindsDBConnector
from endpoints.predict import predict_ns
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

# Initialize Flask-RESTx Api object
api = Api(api_v1, version='0.1.0', title='Mind Reader API', description='API for the Mind Reader backend')

# Register the predict_ns namespace
api.add_namespace(predict_ns)

# Register the API Blueprint
app.register_blueprint(api_v1)

if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logging.StreamHandler())
    app.run(debug=True)
