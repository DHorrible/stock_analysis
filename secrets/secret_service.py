import json


class SecretService:
    def __init__(self):
        with open('secrets/secrets.json', 'r') as f:
            self.__values = json.load(f)

    def get_secret(self, key):
        value = self.__values.get(key, None)
        if value is None:
            raise Exception(f'The secret "{key}" was not found')
        return value


secret_service = SecretService()
