from connectors.mindsdb.connector import Connector


class MindReaderProject:
    PROJECT_NAME = 'mind_reader_project'
    # Get the connection lazily
    server = Connector.connect()

    def __init__(self):
        # self.create_project()
        pass

    def create_project(self):
        return self.server.create_project(self.PROJECT_NAME)

    def get_project(self):
        return self.server.get_project(self.PROJECT_NAME)

    def drop_project(self):
        self.server.drop_project(self.PROJECT_NAME)
