#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
from algorithms import Element

class Test_Element(unittest.TestCase):

    def test_init(self) -> None:
        element = Element(0)
        self.assertEqual(element.value, 0)
        self.assertEqual(element.parent, None)
        self.assertEqual(element.child, None)

    def test_str(self) -> None:
        element = Element('hello, world')

        self.assertEqual(str(element), 'hello, world')

if __name__ == '__main__':
    unittest.main(verbosity=2)
