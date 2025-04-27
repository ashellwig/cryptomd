# Copyright (c) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click

from cryptomd.tools.robinhood.generate_keypair import add_one, generate_keypair


@click.command()
@click.option('-n', '--num', type=int)
def cli_rh_add_one(num: int):
    click.echo(str(add_one(number=num)))


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
