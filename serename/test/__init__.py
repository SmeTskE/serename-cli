__author__ = 'Ruben'

from . import test_scanner
from unittest import TestSuite
from unittest import TextTestRunner

suite = TestSuite([test_scanner.suite()])

if __name__ == '__main__':
    TextTestRunner().run(suite)