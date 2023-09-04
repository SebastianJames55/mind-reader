import os

from connectors.mindsdb.project.mind_reader_project import MindReaderProject


class GPTModel:

    MODEL_ENGINE = 'openai'
    MODEL_NAME = 'text-davinci-003'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    model_name = 'gpt_model'
    project = MindReaderProject().get_project()

    def __init__(self):
        # self.create_model()
        pass

    def create_model(self):
        return self.project.create_model(
            name=self.model_name,
            predict='response',
            engine=self.MODEL_ENGINE,
            options={
                'model_name': self.MODEL_NAME,
                'api_key': self.OPENAI_API_KEY,
                'prompt_template': '''
                    Reply like a friend who cares and wants to help.
                    Input message: {{text}} 
                    In less than 550 characters, when there's some sign of distress in the input share healthy habits, 
                    motivational quotes, inspirational real-life stories. 
                    Provide options to seek out in-person help if you aren't able to satisfy. 
                    Keep the conversation going by asking them to share more. Be a good listener and conversationalist. 
                    In case there's no signs of distress then reply casually like how you would engage in conversation. 
                        ''',
                'max_tokens': 300
            }
        )

    def get_model(self):
        return self.project.get_model(self.model_name)

    def drop_model(self):
        self.project.drop_model(self.model_name)

    def predict(self, data):
        prediction_query = f'''
            SELECT response
            FROM {MindReaderProject.PROJECT_NAME}.{self.model_name}
            WHERE text = "{data}";
        '''
        # Query on the model in the project to make predictions based on data
        query = self.project.query(prediction_query)
        return query.fetch()
