#!/usr/bin/python3
"""unittests for base.py"""

import os
import unitest
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of Base class"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual([b1.id, b2.id, b3.id], [1, 2, 3])


