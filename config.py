import os

# Configuration settings
# Which app to connect to
APP_TO_CONNECT = 'mindsdb'

os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(__file__), 'mind-reader-venv\\Lib\\site-packages'
                                                                           '\\certifi\\cacert.pem')

EMAIL = os.environ.get('MINDSDB_EMAIL')
PASSWORD = os.environ.get('MINDSDB_PASSWORD')
