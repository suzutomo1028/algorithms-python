#!/usr/bin/env python3

import sys, os
import unittest
import random

sys.path.append(os.pardir)
from algorithms import bubble_sort, select_sort, insert_sort, merge_sort, quick_sort

class test_Sort(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [random.randint(0, 99) for _ in range(1000)]
        self.sorted_test_data = sorted(self.test_data)

    def test_bubble_sort(self) -> None:
        sorted_data = bubble_sort(self.test_data)
        self.assertListEqual(sorted_data, self.sorted_test_data)

    def test_select_sort(self) -> None:
        sorted_data = select_sort(self.test_data)
        self.assertListEqual(sorted_data, self.sorted_test_data)

    def test_insert_sort(self) -> None:
        sorted_data = insert_sort(self.test_data)
        self.assertListEqual(sorted_data, self.sorted_test_data)

    def test_merge_sort(self) -> None:
        sorted_data = merge_sort(self.test_data)
        self.assertListEqual(sorted_data, self.sorted_test_data)

    def test_quick_sort(self) -> None:
        sorted_data = quick_sort(self.test_data)
        self.assertListEqual(sorted_data, self.sorted_test_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
