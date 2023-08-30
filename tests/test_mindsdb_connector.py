import unittest
from connectors.mindsdb_connector import drop_project, drop_model, create_project, drop_database, create_database


PROJECT_NAME = 'mind-reader-project'
DB_NAME_IN_MINDSDB = 'yugabyte_demo'


class TestMindsDBConnector(unittest.TestCase):
    def test_create_db(self):
        create_database(DB_NAME_IN_MINDSDB)

    def test_drop_db(self):
        drop_database(DB_NAME_IN_MINDSDB)

    def test_create_project(self):
        create_project(PROJECT_NAME)

    def test_drop_project(self):
        drop_project(PROJECT_NAME)

    def test_drop_model(self):
        model_name = 'gpt_model'
        drop_model(PROJECT_NAME, model_name)


if __name__ == '__main__':
    unittest.main()
