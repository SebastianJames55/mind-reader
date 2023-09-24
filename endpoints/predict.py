from flask import jsonify, g
from flask_restx import Resource, fields, Namespace

from config.general import PROJECT_NAME
from config.model import MODEL_NAME_IN_CONNECTOR
from utils import get_project

predict_ns = Namespace('predict', description='Prediction operations')

request_model = predict_ns.model('RequestModel', {
    'request_message': fields.String(description='Message to get reply to', required=True),
})

# Define a model for the response data
response_model = predict_ns.model('ResponseModel', {
    'response': fields.String(description='Reply from chatbot')
})


class Predict(Resource):
    @predict_ns.doc('predict')
    @predict_ns.expect(request_model, validate=True)
    @predict_ns.response(200, 'Success', response_model)
    def post(self):
        """
        Make a prediction
        """
        try:
            # Data to predict
            data = predict_ns.payload
            request_message = data.get('request_message')

            # Make predictions using the connector and model
            prediction_query = f'''
                SELECT response
                FROM {PROJECT_NAME}.{MODEL_NAME_IN_CONNECTOR}
                WHERE text = "{request_message}";
            '''
            # Query on the model in the project to make predictions based on data
            query = get_project().query(prediction_query)
            prediction = query.fetch()
            prediction_dict = prediction.to_dict(orient='records')
            return prediction_dict, 200

        except Exception as e:
            # Graceful error handling
            error_message = f"An error occurred: {str(e)}"
            return jsonify({'error': error_message}), 500


predict_ns.add_resource(Predict, '/')
