import logging
import os

import mindsdb_sdk

from connectors.base_connector import BaseConnector


def get_mindsdb_connection():
    logging.debug('Connecting to mindsdb app')
    return mindsdb_sdk.connect()


DB_ENGINE = 'mysql'
DB_NAME = 'mysql_demo_db'
DB_CONNECTION_ARGS = {
    "user": "user",
    "password": "example",
    "host": "db-demo-data.example.us-east-1.rds.amazonaws.com",
    "port": "3306",
    "database": "public"
}


def create_database(db_name):
    # Get the connection lazily
    server = get_mindsdb_connection()
    if db_name not in server.list_databases():
        mysql_demo_db = server.create_database(
            engine=DB_ENGINE,
            name=db_name,
            connection_args=DB_CONNECTION_ARGS
        )
        logging.debug('Creating database')
        return mysql_demo_db


def get_database(db_name):
    # Get the connection lazily
    server = get_mindsdb_connection()
    if db_name in server.list_databases():
        logging.debug('Fetching database')
        return server.get_database(db_name)


def drop_database(db_name):
    # Get the connection lazily
    server = get_mindsdb_connection()
    if db_name in server.list_databases():
        logging.debug('Dropping database')
        server.drop_database(db_name)


PROJECT_NAME = 'mind_reader_project'


def get_project_names(server):
    logging.debug('Fetching projects')
    return [project.name for project in server.list_projects()]


def create_project(project_name):
    # Get the connection lazily
    server = get_mindsdb_connection()
    if project_name not in get_project_names(server):
        project = server.create_project(project_name)
        logging.debug('Creating project')
        return project
    else:
        return get_project(project_name)


def get_project(project_name):
    # Get the connection lazily
    server = get_mindsdb_connection()
    if project_name in get_project_names(server):
        logging.debug('Fetching project')
        return server.get_project(project_name)


def drop_project(project_name):
    # Get the connection lazily
    server = get_mindsdb_connection()
    if project_name in get_project_names(server):
        logging.debug('Dropping project')
        server.drop_project(project_name)


MODEL_ENGINE = 'openai'
MODEL_NAME = 'text-davinci-003'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


def get_model_names(project):
    logging.debug('Fetching models')
    return [model.name for model in project.list_models()]


def create_model(project_name, model_name):
    if not is_model_created(project_name, model_name):
        project = get_project(project_name)
        model = project.create_model(
            name=model_name,
            predict='response',
            engine=MODEL_ENGINE,
            options={
                'model_name': MODEL_NAME,
                'api_key': OPENAI_API_KEY,
                'prompt_template': '''
                Reply like a friend who cares and wants to help.
                Input message: {{text}} 
                In less than 550 characters, when there's some sign of distress in the input share healthy habits, 
                motivational quotes, inspirational real-life stories. 
                Provide options to seek out in-person help if you aren't able to satisfy.  
                    ''',
                'max_tokens': 300
            }
        )
        logging.debug('Creating model')
        return model
    else:
        return get_model(project_name, model_name)


def is_model_created(project_name, model_name):
    project = get_project(project_name)
    return model_name in get_model_names(project)


def get_model(project_name, model_name):
    project = get_project(project_name)
    if model_name in get_model_names(project):
        logging.debug('Fetching model')
        return project.get_model(model_name)


def drop_model(project_name, model_name):
    project = get_project(project_name)
    if model_name in get_model_names(project):
        logging.debug('Dropping model')
        project.drop_model(model_name)


class MindsDBConnector(BaseConnector):
    project = create_project(PROJECT_NAME)
    model_name = 'gpt_model'
    model = create_model(PROJECT_NAME, model_name=model_name)

    def __init__(self):
        pass

    def connect(self):
        pass

    def get_db(self):
        pass

    def predict(self, data):
        logging.debug('Sending data for prediction')
        prediction_query = f'''
            SELECT response
            FROM {PROJECT_NAME}.{self.model_name}
            WHERE text = "{data}";
        '''
        # Query on the model in the project to make predictions based on data
        query = self.project.query(prediction_query)
        return query.fetch()
