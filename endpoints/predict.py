from flask import jsonify, g
from flask_restx import Resource, fields, Namespace

predict_ns = Namespace('predict', description='Prediction operations')

resource_model = predict_ns.model('RequestModel', {
    'request_message': fields.String(description='Message to get reply to', required=True),
})

# Define a model for the response data
response_model = predict_ns.model('ResponseModel', {
    'response': fields.String(description='Reply from chatbot')
})


class Predict(Resource):
    @predict_ns.doc('predict')
    @predict_ns.expect(resource_model, validate=True)
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
            prediction = g.connector.predict(request_message)
            prediction_dict = prediction.to_dict(orient='records')
            return prediction_dict, 200

        except Exception as e:
            # Graceful error handling
            error_message = f"An error occurred: {str(e)}"
            return jsonify({'error': error_message}), 500


predict_ns.add_resource(Predict, '/')
