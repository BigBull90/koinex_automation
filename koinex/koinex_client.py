# Author : Shanthi Malladi

# purpose: Koinex platform client
from enum import Enum
import requests
# from utils import print


class KoinexConfig(Enum):
    VALUE = {
        "coins": ['BTC', 'BCH', 'ETH', 'LTC', 'XRP']
    }


class KoinexClient:
    def __init__(self, mode: KoinexConfig) -> None:
        self.config = mode.value

    def get_market_value(self) -> dict:
        reply = requests.get('https://koinex.in/api/ticker')
        if reply.status_code != 200:
            raise Exception("Cannot connect to Koinex Ticker API - Check internet connection")
        else:
            result = dict()
            price = reply.json().get('prices')
            for key in self.config['coins']:
                print("Koinex Price for {} is {}".format(key, price.get(key)))
                result[key] = float(price.get(key))
        return result


if __name__ == '__main__':
    koinex_client = KoinexClient(KoinexConfig.VALUE)
    koinex_client.get_market_value()
