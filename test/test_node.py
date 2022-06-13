#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
from algorithms import Node

class Test_Node(unittest.TestCase):

    def test_init(self) -> None:
        node = Node(0)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)

    def test_str(self) -> None:
        node = Node('hello, world')

        self.assertEqual(str(node), 'hello, world')

if __name__ == '__main__':
    unittest.main(verbosity=2)
