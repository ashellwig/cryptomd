# Copyright (c) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click

from cryptomd.tools.kraken.kraken_ohlcv import print_data
from cryptomd.tools.robinhood.generate_keypair import add_one, generate_keypair


@click.command()
@click.option('-n', '--num', type=int)
def cli_rh_add_one(num: int):
    click.echo(str(add_one(number=num)))


# ---- KRAKEN ----
# Get OHLCV Data
@click.command()
@click.option('-s', '--symbol', type=str)
@click.option('-t', '--timeframe', type=str)
# Get OHLCV data (close) from Kraken exchange.
def cli_kraken_data(symbol: str, timeframe: str):
    last = print_data(symbol=symbol, timeframe=timeframe)
    print('\n' + 'last price: ' + str(last) + '\n')


# ---- ROBINHOOD ----
# Generate keypair
@click.command()
@click.option(
        '-d',
        '--directory',
        type=str,
        help='Where should the output files containing the key data go?'
)
def cli_rh_generate_keypair(directory: str):
    """CLI interface to the generate_keypair function.

    Args:
        directory (str): Directory to output the generated keypair.
    """
    generate_keypair(output_directory_str=directory)
