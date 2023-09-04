import os

from connectors.mindsdb.connector import Connector


class ChatDB:
    DB_ENGINE = 'yugabyte'
    DB_NAME_IN_SOURCE = 'demo'
    SCHEMA_NAME_IN_SOURCE = 'public'
    DB_PORT = 5433
    DB_CONNECTION_ARGS = {
        "user": os.environ.get('DB_USER'),
        "password": os.environ.get('DB_PASSWORD'),
        "host": os.environ.get('DB_HOST'),
        "port": DB_PORT,
        "database": DB_NAME_IN_SOURCE,
        "schema": SCHEMA_NAME_IN_SOURCE
    }

    # Get the connection lazily
    server = Connector.connect()

    def create_database(self, db_name):
        return self.server.create_database(
            engine=self.DB_ENGINE,
            name=db_name,
            connection_args=self.DB_CONNECTION_ARGS
        )

    def get_database(self, db_name):
        return self.server.get_database(db_name)

    def drop_database(self, db_name):
        self.server.drop_database(db_name)
