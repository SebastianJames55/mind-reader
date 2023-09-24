from flask import Blueprint
from flask_restx import Api

from endpoints.predict import predict_ns
from setup import initialize, app

# Create a versioned API Blueprint
api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Initialize Flask-RESTx Api object
api = Api(api_v1, version='0.1.0', title='Mind Reader API', description='API for the Mind Reader backend')

# Register the predict_ns namespace
api.add_namespace(predict_ns)

# Register the API Blueprint
app.register_blueprint(api_v1)

if __name__ == '__main__':
    initialize()
    app.run(debug=False)
