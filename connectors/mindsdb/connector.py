import mindsdb_sdk


class Connector:
    @classmethod
    def connect(cls):
        return mindsdb_sdk.connect()
