#!/usr/bin/env python3

import sys, os
import unittest
import random
import string

sys.path.append(os.pardir)
from algorithms import liner_search, binary_search

class Test_Search(unittest.TestCase):

    def test_liner_search(self) -> None:
        test_int_data = [random.randint(0, 99) for _ in range(100)]
        test_int_key = test_int_data[75]
        index = liner_search(test_int_data, test_int_key)
        self.assertEqual(test_int_data[index], test_int_key)

        test_int_key = -1
        index = liner_search(test_int_data, test_int_key)
        self.assertEqual(index, None)

        test_str_data = [random.choice(string.ascii_letters + string.digits) for _ in range(100)]
        test_str_key = test_str_data[75]
        index = liner_search(test_str_data, test_str_key)
        self.assertEqual(test_str_data[index], test_str_key)

        test_str_key = '@'
        index = liner_search(test_str_data, test_str_key)
        self.assertEqual(index, None)

    def test_binary_search(self) -> None:
        test_int_data = [x for x in range(100)]
        test_int_key = test_int_data[75]
        index = binary_search(test_int_data, test_int_key)
        self.assertEqual(test_int_data[index], test_int_key)

        test_int_key = -1
        index = binary_search(test_int_data, test_int_key)
        self.assertEqual(index, None)

        test_str_data = 'abcdefghijklmnopqrstuvwxyz'
        test_str_key = test_str_data[10]
        index = binary_search(test_str_data, test_str_key)
        self.assertEqual(test_str_data[index], test_str_key)

        test_str_key = '@'
        index = binary_search(test_str_data, test_str_key)
        self.assertEqual(index, None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
