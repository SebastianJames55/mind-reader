import unittest
from connectors.mindsdb_connector import drop_project


PROJECT_NAME = 'mind-reader-project'


class TestMindsDBConnector(unittest.TestCase):
    def test_drop_project(self):
        drop_project(PROJECT_NAME)


if __name__ == '__main__':
    unittest.main()
