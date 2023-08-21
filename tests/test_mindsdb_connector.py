import unittest
from connectors.mindsdb_connector import drop_project, drop_model


PROJECT_NAME = 'mind_reader_project'


class TestMindsDBConnector(unittest.TestCase):
    def test_drop_project(self):
        drop_project(PROJECT_NAME)

    def test_drop_model(self):
        model_name = 'gpt_model'
        drop_model(PROJECT_NAME, model_name)


if __name__ == '__main__':
    unittest.main()
