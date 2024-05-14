#Source: https://stackoverflow.com/questions/48224245/typeerror-string-argument-without-an-encoding-in-3-4-but-not-in-3-6
#! /usr/bin/env python3

from base64 import b64decode
from lzma import LZMADecompressor
from sys import version


class B64LZMA(str):
    """A string of base64 encoded, LZMA compressed data."""

    def __bytes__(self):
        """Returns the decompressed data."""
        return LZMADecompressor().decompress(b64decode(self.encode()))

    def __str__(self):
        """Returns the string decoded from __bytes__."""
        return bytes(self).decode()


TEST_STR = B64LZMA('/Td6WFoAAATm1rRGAgAhARYAAAB0L+WjAQALSGVsbG8gd29ybGQuAGt+oFiSvoAYAAEkDKYY2NgftvN9AQAAAAAEWVo=')

if __name__ == '__main__':
    print(version)
    print(TEST_STR)