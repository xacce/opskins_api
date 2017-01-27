import requests


class Endpoint(object):
    request = None

    def __init__(self, api_key):
        self._api_key = api_key

    def query(self):
        url = 'https://opskins.com/api/user_api.php?request={request}&key={code}'.format(request=self.request, code=self._api_key)
        response = requests.get(url).json()

        return self.format(response)

    def format(self, response):
        raise NotImplementedError()
