from flask import Flask, jsonify, g, Blueprint
from flask_restx import Api, Resource
import config
from connectors.base_connector import BaseConnector
from models.base_model import BaseModel
from connectors import MindsDBConnector
from models import MindsDBModel

app = Flask(__name__)


# Function to get the connector based on the specified app in config.py
def get_connector():
    # Create a connector based on the specified app in config.py
    if config.APP_TO_CONNECT == 'mindsdb':
        return MindsDBConnector()
    else:
        raise ValueError("Invalid app specified in config.py")


# Function to get the model based on the specified app in config.py
def get_model():
    if config.APP_TO_CONNECT == 'mindsdb':
        return MindsDBModel()
    else:
        raise ValueError("Invalid app specified in config.py")


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
            # Assuming you have some data to predict, replace data with the actual data
            data = {
                'feature1': 10,
                'feature2': 20,
                # Add more features here as needed
            }

            # Connect to the app using the connector
            g.connector.connect()

            # Train the model (optional, depending on the app)
            g.model.train(data)

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
