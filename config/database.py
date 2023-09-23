import os

# Data source to connect to
DB_ENGINE = 'yugabyte'
# Name of the database in source
DB_NAME_IN_SOURCE = 'demo'
# Name of the schema in source database
SCHEMA_NAME_IN_SOURCE = 'public'
# Port at which database is available
DB_PORT = 5433
# Database connection arguments
DB_CONNECTION_ARGS = {
    # User name
    "user": os.environ.get('DB_USER'),
    # Password for the user
    "password": os.environ.get('DB_PASSWORD'),
    # Url where database is available
    "host": os.environ.get('DB_HOST'),
    # Port to connect to database
    "port": DB_PORT,
    # Database name
    "database": DB_NAME_IN_SOURCE,
    # Schema name
    "schema": SCHEMA_NAME_IN_SOURCE
}
# Name to be given to DB in the connector
DB_NAME_IN_CONNECTOR = 'yugabyte_demo'

# Name of the chat input table in DB
CHAT_INPUT_TABLE = 'chat_input_table'
