# Author: Shanthi Malladi
# Purpose: Business logic

from time import sleep

from bitrex_custom.biterx_client import BittrexConfig, BittrexClient
from koinex.koinex_client import KoinexConfig, KoinexClient
from utils import logger, CONFIG_BITCOIN


# if __name__ == '__main__':
def run_program() -> None:
    logger("################ Bittrex ################")
    bitrex_client = BittrexClient(BittrexConfig.VALUE)
    bitrex_market_details = bitrex_client.get_current_market()
    logger("################ Koinex ################")
    koinex_client = KoinexClient(KoinexConfig.VALUE)
    koinex_details = koinex_client.get_market_value()
    logger("################ Available coins in Bittrex ################")
    bitrex_client.get_available_coin_volume()
    if CONFIG_BITCOIN.get('bitcoin_buy_price'):
        btc_value = float(CONFIG_BITCOIN.get('bitcoin_buy_price'))
    else:
        btc_value = koinex_details.get("BTC")
    logger("################ Buy price of Cryptos ################")
    bitrex_bcc_price = btc_value * bitrex_market_details.get("BTC-BCC")
    bitrex_eth_price = btc_value * bitrex_market_details.get("BTC-ETH")
    bitrex_ltc_price = btc_value * bitrex_market_details.get("BTC-LTC")
    bitrex_xrp_price = btc_value * bitrex_market_details.get("BTC-XRP")
    print("bitrex_bcc * btc_koinex is {}".format(bitrex_bcc_price))
    print("bitrex_eth * btc_koinex is {}".format(bitrex_eth_price))
    print("bitrex_ltc * btc_koinex is {}".format(bitrex_ltc_price))
    print("bitrex_xrp * btc_koinex is {}".format(bitrex_xrp_price))

    koinex_bch_per_unit = koinex_details.get("BCH") - btc_value * bitrex_market_details.get("BTC-BCC")
    koinex_eth_per_unit = koinex_details.get("ETH") - btc_value * bitrex_market_details.get("BTC-ETH")
    koinex_ltc_per_unit = koinex_details.get("LTC") - btc_value * bitrex_market_details.get("BTC-LTC")
    koinex_xrp_per_unit = koinex_details.get("XRP") - btc_value * bitrex_market_details.get("BTC-XRP")

    logger("################ Profit per unit details ################")
    print("profit for unit bch {}".format(koinex_bch_per_unit))
    print("profit for unit eth {}".format(koinex_eth_per_unit))
    print("profit for unit ltc {}".format(koinex_ltc_per_unit))
    print("profit for unit xrp {}".format(koinex_xrp_per_unit))

    logger("################ Profit per 1 Lakh details ################")
    print("profit per 1 Lakh for bch {}".format((koinex_bch_per_unit * 100000) / bitrex_bcc_price))
    print("profit per 1 Lakh for eth {}".format((koinex_eth_per_unit * 100000) / bitrex_eth_price))
    print("profit per 1 Lakh for ltc {}".format((koinex_ltc_per_unit * 100000) / bitrex_ltc_price))
    print("profit per 1 Lakh for xrp {}".format((koinex_xrp_per_unit * 100000) / bitrex_xrp_price))

    btc_investment = CONFIG_BITCOIN.get('invested_amount')
    if btc_investment:
        logger("################ Profit for your {} investment ################".format(btc_investment))
        print("profit for your investment for bch is {}".format((koinex_bch_per_unit * btc_investment) / bitrex_bcc_price))
        print("profit for your investment for eth is {}".format((koinex_eth_per_unit * btc_investment) / bitrex_eth_price))
        print("profit for your investment for ltc is {}".format((koinex_ltc_per_unit * btc_investment) / bitrex_ltc_price))
        print("profit for your investment for xrp is {}".format((koinex_xrp_per_unit * btc_investment) / bitrex_xrp_price))


if __name__ == '__main__':
    while True:
        logger("############# Another run starting ###############")
        run_program()
        sleep(2*60)
