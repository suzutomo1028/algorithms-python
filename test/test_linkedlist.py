#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
from algorithms import LinkedList

class Test_LinkedList(unittest.TestCase):

    def test_init(self) -> None:
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.count, 0)
        self.assertEqual(linkedlist.is_empty, True)
        self.assertListEqual(linkedlist.to_list(), [])

    def test_append(self) -> None:
        linkedlist = LinkedList()

        linkedlist.append(0)
        self.assertEqual(linkedlist.count, 1)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0])

        linkedlist.append(1)
        self.assertEqual(linkedlist.count, 2)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1])

    def test_bulk_append(self) -> None:
        linkedlist = LinkedList()

        linkedlist.bulk_append([0, 1, 2])
        self.assertEqual(linkedlist.count, 3)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1, 2])

        linkedlist.bulk_append([3, 4, 5])
        self.assertEqual(linkedlist.count, 6)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1, 2, 3, 4, 5])

        with self.assertRaises(TypeError):
            linkedlist.bulk_append(0)

    def test_insert(self) -> None:
        linkedlist = LinkedList()
        linkedlist.append(2)

        linkedlist.insert(0, 0)
        self.assertEqual(linkedlist.count, 2)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 2])

        linkedlist.insert(1, 1)
        self.assertEqual(linkedlist.count, 3)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1, 2])

        with self.assertRaises(IndexError):
            linkedlist.insert(-1, -1)

        with self.assertRaises(IndexError):
            linkedlist.insert(3, 3)

    def test_bulk_insert(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([6, 7, 8])

        linkedlist.bulk_insert(0, [0, 1, 2])
        self.assertEqual(linkedlist.count, 6)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1, 2, 6, 7, 8])

        linkedlist.bulk_insert(3, [3, 4, 5])
        self.assertEqual(linkedlist.count, 9)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8])

        with self.assertRaises(IndexError):
            linkedlist.bulk_insert(-1, [-3, -2, -1])

        with self.assertRaises(IndexError):
            linkedlist.bulk_insert(9, [9, 10, 11])

        with self.assertRaises(TypeError):
            linkedlist.bulk_insert(0, -1)

    def test_remove(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([0, 1, 2, 3])

        linkedlist.remove(0)
        self.assertEqual(linkedlist.count, 3)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [1, 2, 3])

        linkedlist.remove(1)
        self.assertEqual(linkedlist.count, 2)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [1, 3])

        linkedlist.remove(1)
        self.assertEqual(linkedlist.count, 1)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [1])

        linkedlist.remove(0)
        self.assertEqual(linkedlist.count, 0)
        self.assertEqual(linkedlist.is_empty, True)
        self.assertListEqual(linkedlist.to_list(), [])

        with self.assertRaises(IndexError):
            linkedlist.remove(-1)

        with self.assertRaises(IndexError):
            linkedlist.remove(0)

    def test_bulk_remove(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([0, 1, 2, 3, 4, 5, 6, 7, 8])

        linkedlist.bulk_remove(0, 0)
        self.assertEqual(linkedlist.count, 9)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8])

        linkedlist.bulk_remove(0, 2)
        self.assertEqual(linkedlist.count, 7)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [2, 3, 4, 5, 6, 7, 8])

        linkedlist.bulk_remove(3, 2)
        self.assertEqual(linkedlist.count, 5)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [2, 3, 4, 7, 8])

        linkedlist.bulk_remove(3, 2)
        self.assertEqual(linkedlist.count, 3)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [2, 3, 4])

        linkedlist.bulk_remove(0, 3)
        self.assertEqual(linkedlist.count, 0)
        self.assertEqual(linkedlist.is_empty, True)
        self.assertListEqual(linkedlist.to_list(), [])

        with self.assertRaises(IndexError):
            linkedlist.bulk_remove(-1, 0)

        with self.assertRaises(IndexError):
            linkedlist.bulk_remove(0, 0)

        linkedlist.append(0)

        with self.assertRaises(ValueError):
            linkedlist.bulk_remove(0, -1)

        with self.assertRaises(ValueError):
            linkedlist.bulk_remove(0, 2)

    def test_clear(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([0, 1, 2])

        linkedlist.clear()
        self.assertEqual(linkedlist.count, 0)
        self.assertEqual(linkedlist.is_empty, True)
        self.assertListEqual(linkedlist.to_list(), [])

    def test_add(self) -> None:
        linkedlist_a = LinkedList()
        linkedlist_a.bulk_append([0, 1, 2])
        linkedlist_b = LinkedList()
        linkedlist_b.bulk_append([3, 4, 5])
        linkedlist_c = LinkedList()

        linkedlist_c = linkedlist_a + linkedlist_b
        self.assertEqual(linkedlist_c.count, 6)
        self.assertEqual(linkedlist_c.is_empty, False)
        self.assertListEqual(linkedlist_c.to_list(), [0, 1, 2, 3, 4, 5])

        with self.assertRaises(TypeError):
            linkedlist_c = linkedlist_a + 3

    def test_iadd(self) -> None:
        linkedlist_a = LinkedList()
        linkedlist_a.bulk_append([0, 1, 2])
        linkedlist_b = LinkedList()
        linkedlist_b.bulk_append([3, 4, 5])

        linkedlist_a += linkedlist_b
        self.assertEqual(linkedlist_a.count, 6)
        self.assertEqual(linkedlist_a.is_empty, False)
        self.assertListEqual(linkedlist_a.to_list(), [0, 1, 2, 3, 4, 5])

        with self.assertRaises(TypeError):
            linkedlist_a += 6

    def test_getitem(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([0, 1, 2])

        value = linkedlist[0]
        self.assertEqual(value, 0)

        value = linkedlist[1]
        self.assertEqual(value, 1)

        value = linkedlist[2]
        self.assertEqual(value, 2)

        with self.assertRaises(IndexError):
            value = linkedlist[-1]

        with self.assertRaises(IndexError):
            value = linkedlist[3]

    def test_setitem(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([3, 4, 5])

        linkedlist[0] = 0
        self.assertEqual(linkedlist[0], 0)

        linkedlist[1] = 1
        self.assertEqual(linkedlist[1], 1)

        linkedlist[2] = 2
        self.assertEqual(linkedlist[2], 2)

        with self.assertRaises(IndexError):
            linkedlist[-1] = -1

        with self.assertRaises(IndexError):
            linkedlist[3] = 3

    def test_next(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([0, 1, 2])

        value = next(linkedlist)
        self.assertEqual(value, 0)

        value = next(linkedlist)
        self.assertEqual(value, 1)

        value = next(linkedlist)
        self.assertEqual(value, 2)

        with self.assertRaises(StopIteration):
            value = next(linkedlist)

    def test_iter(self) -> None:
        linkedlist = LinkedList()
        linkedlist.bulk_append([0, 1, 2])

        for i, value in enumerate(linkedlist):
            self.assertEqual(value, linkedlist[i])

        for i, value in enumerate(linkedlist):
            self.assertEqual(value, linkedlist[i])

    def test_from_iterable(self) -> None:
        linkedlist = LinkedList.from_iterable([0, 1, 2])
        self.assertEqual(linkedlist.count, 3)
        self.assertEqual(linkedlist.is_empty, False)
        self.assertListEqual(linkedlist.to_list(), [0, 1, 2])

        with self.assertRaises(TypeError):
            linkedlist = LinkedList.from_iterable(0)

    def test_to_list(self) -> None:
        linkedlist = LinkedList.from_iterable([0, 1, 2])

        self.assertListEqual(linkedlist.to_list(), [0, 1, 2])

    def test_clone(self) -> None:
        linkedlist_a = LinkedList.from_iterable([0, 1, 2])

        linkedlist_b = linkedlist_a.clone()
        self.assertIsNot(linkedlist_b, linkedlist_a)
        self.assertListEqual(linkedlist_b.to_list(), linkedlist_a.to_list())

    def test_get_range(self) -> None:
        linkedlist_a = LinkedList.from_iterable([0, 1, 2, 3, 4, 5])

        linkedlist_b = linkedlist_a.get_range(0, 0)
        self.assertListEqual(linkedlist_b.to_list(), [])

        linkedlist_b = linkedlist_a.get_range(0, 3)
        self.assertListEqual(linkedlist_b.to_list(), [0, 1, 2])

        linkedlist_b = linkedlist_a.get_range(3, 3)
        self.assertListEqual(linkedlist_b.to_list(), [3, 4, 5])

        with self.assertRaises(IndexError):
            linkedlist_b = linkedlist_a.get_range(-1, 0)

        with self.assertRaises(IndexError):
            linkedlist_b = linkedlist_a.get_range(6, 0)

        with self.assertRaises(ValueError):
            linkedlist_b = linkedlist_a.get_range(0, -1)

        with self.assertRaises(ValueError):
            linkedlist_b = linkedlist_a.get_range(0, 7)

    def test_str(self) -> None:
        linkedlist = LinkedList.from_iterable([0, 1, 2])

        self.assertEqual(str(linkedlist), '[0, 1, 2]')

if __name__ == '__main__':
    unittest.main(verbosity=2)
