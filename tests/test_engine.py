#!/usr/bin/env python

"""
Tests for `plumbery` module.
"""

import os
import unittest

from plumbery.engine import PlumberyEngine

os.environ['SHARED_SECRET'] = "WhatsUpDoc"

class TestPlumberyEngine(unittest.TestCase):

    def setUp(self):
        self.engine = PlumberyEngine()

    def tearDown(self):
        self.engine = None

    def test_000_something(self):
        pass


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())