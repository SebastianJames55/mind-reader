from flask import Flask, g, Blueprint
from flask_restx import Api

import config
import constants
from connectors.mindsdb.project.gpt_model import GPTModel
from endpoints.predict import predict_ns

app = Flask(__name__)


# Function to get the connector based on the specified app in config.py
def get_connector():
    # Create a connector based on the specified app in config.py
    if config.APP_TO_CONNECT == constants.MINDSDB:
        return GPTModel()
    else:
        raise ValueError(constants.INVALID_APP_MESSAGE)


@app.before_request
def before_request():
    # Set the connector and model instances as application context variables
    g.model = get_connector()


# Create a versioned API Blueprint
api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Initialize Flask-RESTx Api object
api = Api(api_v1, version='0.1.0', title='Mind Reader API', description='API for the Mind Reader backend')

# Register the predict_ns namespace
api.add_namespace(predict_ns)

# Register the API Blueprint
app.register_blueprint(api_v1)

if __name__ == '__main__':
    app.run(debug=True)
