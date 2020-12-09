# from http.client import HTTPConnection as HttpClient
from tinvest import SyncClient, OpenApi


from secrets.secret_service import secret_service
from http import HTTPStatus
from typing import Any, List


class HTTPError(Exception):
    pass


class CustomClient(SyncClient):
    def request(self, *args, **kwargs) -> Any:
        response = super().request(*args, **kwargs)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.parse_error().json())

        return response.parse_json().payload


class TinkoffConnector:
    def __init__(self):
        self.__api_key = secret_service.get_secret('tinkoff_api_token')
        self.__client = CustomClient(self.__api_key, use_sandbox=False)
        self.__api = OpenApi(self.__client)

    def check_tickets(self, tickets) -> List:
        resp = self.__api.market.market_stocks_get()
        print(resp)
