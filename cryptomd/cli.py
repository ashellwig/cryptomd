# Copyright (c) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click

from cryptomd.tools.cli import cli_rh_add_one, cli_rh_generate_keypair


@click.group()
def cli():
    pass


cli.add_command(cli_rh_add_one, name='add-one')
cli.add_command(cli_rh_generate_keypair, name='gen-keypair')

if __name__ == '__main__':
    cli()
