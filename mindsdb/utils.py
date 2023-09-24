import mindsdb_sdk
from config.general import *


server = mindsdb_sdk.connect(login=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)


def get_project():
    return server.get_project(PROJECT_NAME)


def is_project_created(project_name):
    return project_name in [project.name for project in server.list_projects()]


def is_model_created(model_name):
    return model_name in [model.name for model in get_project().list_models()]


def is_db_created(db_name):
    return db_name in [db.name for db in server.list_databases()]
