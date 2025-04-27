# Copyright (c) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from cryptomd.tools.robinhood.generate_keypair import add_one


def test_add():
    assert add_one(1) == 2
