# Author: Shanthi Malladi

# Purpose: Bittrex platform client

from enum import Enum

from bittrex import Bittrex


# from utils import print


class BittrexConfig(Enum):
    VALUE = {
        "monitor_markets": ['BTC-BCC', 'BTC-ETH', 'BTC-LTC', 'BTC-XRP'],
        "available_coins": ['BTC', 'BCC', 'ETH', 'LTC', 'XRP']
    }


class BittrexClient:
    def __init__(self, config: BittrexConfig):
        self.config = config.value
        self.bitrex_client = Bittrex(api_key='e89bdfda454946c38d31640c16c5f3ba',
                                     api_secret='82ae01deaa934d9a9d164678718fbd25')

    def get_available_coin_volume(self) -> None:
        coins = self.config['available_coins']
        for coin in coins:
            btc_volume_dict = self.bitrex_client.get_balance(coin)
            # data = json.load(btc_volume_json)
            btc_volume_dict = self._parse_result(btc_volume_dict)
            # for header, value in btc_volume_dict.items():
            #     print("{x} {y}".format(x=header, y=value))
            if btc_volume_dict.get('Available'):
                print('Available {0:} in your account is {1:0.10f}'.format(coin, btc_volume_dict.get('Available')))
            else:
                print('Available {0:} in your account is {1:}'.format(coin, btc_volume_dict.get('Available')))

    def get_current_market(self) -> dict:
        markets = self.config['monitor_markets']
        result = dict()
        for market in markets:
            market_name = None
            while market != market_name:
                market_name, ask_value = self.get_market(market)
            result.update({market_name: ask_value})
        return result

    def get_market(self, market) -> tuple:
        result = dict()
        market_value = self.bitrex_client.get_marketsummary(market=market)
        market_value = self._parse_result(market_value)
        ask_value = market_value[0].get('Last')
        market_name = market_value[0].get('MarketName')
        print("Last Traded value of {0:} is {1:0.10f}".format(market_name, ask_value))
        result[market_name] = ask_value
        return market_name, ask_value

    @staticmethod
    def _parse_result(raw_response: dict) -> dict:
        # Todo: check response status to be success
        response = raw_response['result']
        return response


if __name__ == '__main__':
    bitrex_client = BittrexClient(BittrexConfig.VALUE)
    bitrex_client.get_bitcoin_price()
