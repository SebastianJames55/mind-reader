from flask import Flask

from config.model import *
from config.general import PROJECT_NAME
from config.database import *
from utils import server, is_project_created, is_model_created, is_db_created

app = Flask(__name__)


def initialize():
    project = server.get_project(PROJECT_NAME) if is_project_created(PROJECT_NAME) else server \
        .create_project(PROJECT_NAME)
    project.get_model(MODEL_NAME_IN_CONNECTOR) if is_model_created(MODEL_NAME_IN_CONNECTOR) \
        else project.create_model(
        name=MODEL_NAME_IN_CONNECTOR,
        predict='response',
        engine=MODEL_ENGINE,
        options={
            'model_name': MODEL_NAME,
            'api_key': OPENAI_API_KEY,
            'prompt_template': '''
                        Hello there, I'm here to provide support and information during tough times. 
                        Whether you have questions, need encouragement, or seek resources, I'm here for you. 
                        Please share what's on your mind, and I'll do my best to assist you. Remember, you're not alone,
                        and together, we can navigate through challenges with strength and resilience.
                        If you're feeling down, just let me know, and I'll provide uplifting words of encouragement. 
                        If you have specific questions or need information, feel free to ask. 
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
    server.get_database(DB_NAME_IN_CONNECTOR) if is_db_created(DB_NAME_IN_CONNECTOR) else server \
        .create_database(
        engine=DB_ENGINE,
        name=DB_NAME_IN_CONNECTOR,
        connection_args=DB_CONNECTION_ARGS
    )
