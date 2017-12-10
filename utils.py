# Author: Shanthi Malladi
# Purpose: Utils for smooth run
from datetime import datetime

DatetimeFormat = '%H:%M:%S %Y:%m:%d'
float_format = '0.10f'

CONFIG_BITCOIN = {
    "bitcoin_buy_price": None,
    "invested_amount": None
}


def logger(msg: str) -> None:
    print('\n{x} {y}\n'.format(x=datetime.now().strftime(DatetimeFormat), y=msg))
