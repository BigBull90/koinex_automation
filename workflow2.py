from bitrex_custom.biterx_client import BittrexClient, BittrexConfig
from koinex.koinex_client import KoinexClient, KoinexConfig
from exchanges.bitfinex import Bitfinex

CONFIG = {
    "BCH": "BTC-BCC",
    "ETH": "BTC-ETH",
    "XRP": "BTC-XRP"
}
transaction_mode = "XRP"

VALUE = ["BTC"]
if __name__ == '__main__':

    koinex_client = KoinexClient(KoinexConfig.VALUE)

    koinex_market_values = koinex_client.get_market_value()

    for value in VALUE:
        koinex_value = koinex_market_values.get(value)
        bitfinex_client = Bitfinex()
        current_btc_value = bitfinex_client.get_current_price()
        inr_btc_value = int(current_btc_value) * 64.52
        print(koinex_value, inr_btc_value)
