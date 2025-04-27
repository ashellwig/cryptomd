# Copyright (c) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import asciichartpy
import ccxt


def print_data(symbol, timeframe):
    exchange: ccxt.kraken = ccxt.kraken()
    symbol: str = 'BTC/USD'

    index: int = 4

    length: int = 80
    height: int = 15

    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

    series = [x[index] for x in ohlcv]

    for x in ohlcv:
        print(exchange.iso8601(x[0]), x)

    print('\n' + exchange.name + ' ' + symbol + ' ' + timeframe + ' chart:')

    # print the chart
    print('\n' + asciichartpy.plot(series[-length:], {'height': height}))

    last = ohlcv[len(ohlcv) - 1][index]  # last closing price
    return last
