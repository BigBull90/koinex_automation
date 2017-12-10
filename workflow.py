# Author: Shanthi Malladi
# Purpose: Business logic

from time import sleep

from bitrex_custom.biterx_client import BittrexConfig, BittrexClient
from koinex.koinex_client import KoinexConfig, KoinexClient
from utils import logger, CONFIG_BITCOIN


class ProfitRun:
    def __init__(self) -> None:
        self.bittrex_client = BittrexClient(BittrexConfig.VALUE)
        self.koinex_client = KoinexClient(KoinexConfig.VALUE)

    def get_bittrex_volume_status(self) -> None:
        logger("################ Available coins in Bittrex ################")
        self.bittrex_client.get_available_coin_volume()

    def get_koinex_stats(self) -> None:
        logger("################ Koinex Statastics #################")
        stats_dict = self.koinex_client.get_market_stats()
        for coin in stats_dict:
            max_value = stats_dict.get(coin).get('max_24hrs')
            min_value = stats_dict.get(coin).get('min_24hrs')
            avg_value = (min_value + max_value) / 2
            print("{coin_name}:".format(coin_name=coin) +
                  " 24-Highest: {highest},".format(highest=max_value) +
                  " 24-Lowest: {lowest},".format(lowest=min_value) +
                  "Average price: {average}".format(average=avg_value)
                  )

    def run_program(self) -> None:
        logger("################ Bittrex ################")
        bitrex_market_details = self.bittrex_client.get_current_market()

        logger("################ Koinex ################")
        koinex_details = self.koinex_client.get_market_value()

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
            print("profit for your investment for bch is {}".format(
                (koinex_bch_per_unit * btc_investment) / bitrex_bcc_price))
            print("profit for your investment for eth is {}".format(
                (koinex_eth_per_unit * btc_investment) / bitrex_eth_price))
            print("profit for your investment for ltc is {}".format(
                (koinex_ltc_per_unit * btc_investment) / bitrex_ltc_price))
            print("profit for your investment for xrp is {}".format(
                (koinex_xrp_per_unit * btc_investment) / bitrex_xrp_price))


if __name__ == '__main__':
    run_client = ProfitRun()
    while True:
        logger("############# Another run starting ###############")
        run_client.run_program()
        run_client.get_koinex_stats()
        sleep(2 * 60)
