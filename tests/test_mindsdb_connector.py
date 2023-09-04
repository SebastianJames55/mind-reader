import unittest

from connectors.mindsdb.database.chat_db import ChatDB
from connectors.mindsdb.project.gpt_model import GPTModel
from connectors.mindsdb.project.mind_reader_project import MindReaderProject

DB_NAME_IN_MINDSDB = 'yugabyte_demo'
project = MindReaderProject()
db = ChatDB()
chat_model = GPTModel()


class TestMindsDBConnector(unittest.TestCase):
    def test_create_db(self):
        db.create_database(DB_NAME_IN_MINDSDB)

    def test_drop_db(self):
        db.drop_database(DB_NAME_IN_MINDSDB)

    def test_create_project(self):
        project.create_project()

    def test_drop_project(self):
        project.drop_project()

    def test_drop_model(self):
        chat_model.drop_model()


if __name__ == '__main__':
    unittest.main()
