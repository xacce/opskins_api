from api import Endpoint
import datetime


class ActiveSaleRow(object):
    _timestamp_row_name = 'sale_time'

    def __init__(self, raw):
        self._raw = raw

    @property
    def amount(self):
        return float(self._raw['amount']) / 100

    @property
    def sale_time(self):
        return datetime.datetime.fromtimestamp(int(self._raw['sale_time']))

    @property
    def hash_name(self):
        return self._raw['market_name']

    @property
    def id(self):
        return self._raw['id']


class GetActiveSales(Endpoint):
    request = 'GetActiveSales'

    def format(self, response):
        for item in response['result']:
            yield ActiveSaleRow(item)
