#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
from algorithms import BinaryTree

class Test_BinaryTree(unittest.TestCase):

    def test_init(self) -> None:
        binarytree = BinaryTree()
        self.assertEqual(binarytree.count, 0)
        self.assertEqual(binarytree.is_empty, True)
        self.assertListEqual(binarytree.to_list(), [])

    def test_insert(self) -> None:
        binarytree = BinaryTree()

        binarytree.insert(3)
        self.assertEqual(binarytree.count, 1)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [3])

        binarytree.insert(1)
        self.assertEqual(binarytree.count, 2)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[1], 3])

        binarytree.insert(0)
        self.assertEqual(binarytree.count, 3)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1], 3])

        binarytree.insert(2)
        self.assertEqual(binarytree.count, 4)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3])

        binarytree.insert(5)
        self.assertEqual(binarytree.count, 5)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3, [5]])

        binarytree.insert(6)
        self.assertEqual(binarytree.count, 6)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3, [5, [6]]])

        binarytree.insert(4)
        self.assertEqual(binarytree.count, 7)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3, [[4], 5, [6]]])

    def test_bulk_insert(self) -> None:
        binarytree = BinaryTree()

        binarytree.bulk_insert([])
        self.assertEqual(binarytree.count, 0)
        self.assertEqual(binarytree.is_empty, True)
        self.assertListEqual(binarytree.to_list(), [])

        binarytree.bulk_insert([3, 1, 0, 2])
        self.assertEqual(binarytree.count, 4)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3])

        binarytree.bulk_insert([5, 6, 4])
        self.assertEqual(binarytree.count, 7)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3, [[4], 5, [6]]])

        with self.assertRaises(TypeError):
            binarytree.bulk_insert(7)

    def test_min(self) -> None:
        binarytree = BinaryTree()
        binarytree.bulk_insert([3, 1, 0, 2, 5, 6, 4])

        value = binarytree.min()
        self.assertEqual(value, 0)

        binarytree = BinaryTree()

        with self.assertRaises(RuntimeError):
            value = binarytree.min()

    def test_max(self) -> None:
        binarytree = BinaryTree()
        binarytree.bulk_insert([3, 1, 0, 2, 5, 6, 4])

        value = binarytree.max()
        self.assertEqual(value, 6)

        binarytree = BinaryTree()

        with self.assertRaises(RuntimeError):
            value = binarytree.max()

    def test_remove_min(self) -> None:
        binarytree = BinaryTree()
        binarytree.bulk_insert([3, 1, 0, 2, 5, 6, 4])

        binarytree.remove_min()
        self.assertEqual(binarytree.count, 6)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[1, [2]], 3, [[4], 5, [6]]])

        binarytree = BinaryTree()

        with self.assertRaises(RuntimeError):
            binarytree.remove_min()

    def test_remove_max(self) -> None:
        binarytree = BinaryTree()
        binarytree.bulk_insert([3, 1, 0, 2, 5, 6, 4])

        binarytree.remove_max()
        self.assertEqual(binarytree.count, 6)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3, [[4], 5]])

        binarytree = BinaryTree()

        with self.assertRaises(RuntimeError):
            binarytree.remove_max()

    def test_remove(self) -> None:
        binarytree = BinaryTree()
        binarytree.bulk_insert([3, 1, 0, 2, 5, 6, 4])

        binarytree.remove(1)
        self.assertEqual(binarytree.count, 6)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 2], 3, [[4], 5, [6]]])

        binarytree.remove(5)
        self.assertEqual(binarytree.count, 5)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 2], 3, [[4], 6]])

        binarytree.remove(3)
        self.assertEqual(binarytree.count, 4)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 2], 4, [6]])

        binarytree.remove(0)
        self.assertEqual(binarytree.count, 3)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[2], 4, [6]])

        binarytree.remove(6)
        self.assertEqual(binarytree.count, 2)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[2], 4])

        binarytree.remove(4)
        self.assertEqual(binarytree.count, 1)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [2])

        binarytree.remove(2)
        self.assertEqual(binarytree.count, 0)
        self.assertEqual(binarytree.is_empty, True)
        self.assertListEqual(binarytree.to_list(), [])

        with self.assertRaises(RuntimeError):
            binarytree.remove(7)

    def test_clear(self) -> None:
        binarytree = BinaryTree()
        binarytree.bulk_insert([3, 1, 0, 2, 5, 6, 4])

        binarytree.clear()
        self.assertEqual(binarytree.count, 0)
        self.assertEqual(binarytree.is_empty, True)
        self.assertListEqual(binarytree.to_list(), [])

    def test_depth(self) -> None:
        binarytree = BinaryTree()

        binarytree.insert(3)

        depth = binarytree.depth()
        self.assertEqual(depth, 0)

        binarytree.insert(1)

        depth = binarytree.depth()
        self.assertEqual(depth, 1)

        binarytree.insert(0)

        depth = binarytree.depth()
        self.assertEqual(depth, 2)

        binarytree.insert(2)

        depth = binarytree.depth()
        self.assertEqual(depth, 2)

        binarytree.insert(5)

        depth = binarytree.depth()
        self.assertEqual(depth, 2)

        binarytree.insert(6)

        depth = binarytree.depth()
        self.assertEqual(depth, 2)

        binarytree.insert(4)

        depth = binarytree.depth()
        self.assertEqual(depth, 2)

        binarytree.clear()

        with self.assertRaises(RuntimeError):
            depth = binarytree.depth()

    def test_from_iterable(self) -> None:
        binarytree = BinaryTree.from_iterable([3, 1, 0, 2, 5, 6, 4])
        self.assertEqual(binarytree.count, 7)
        self.assertEqual(binarytree.is_empty, False)
        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3, [[4], 5, [6]]])

        with self.assertRaises(TypeError):
            binarytree = BinaryTree.from_iterable(0)

    def test_to_list(self) -> None:
        binarytree = BinaryTree.from_iterable([3, 1, 0, 2, 5, 6, 4])

        self.assertListEqual(binarytree.to_list(), [[[0], 1, [2]], 3, [[4], 5, [6]]])

    def test_clone(self) -> None:
        binarytree_a = BinaryTree.from_iterable([3, 1, 0, 2, 5, 6, 4])

        binarytree_b = binarytree_a.clone()
        self.assertIsNot(binarytree_b, binarytree_a)
        self.assertListEqual(binarytree_b.to_list(), binarytree_a.to_list())

    def test_str(self) -> None:
        binarytree = BinaryTree.from_iterable([3, 1, 0, 2, 5, 6, 4])

        self.assertEqual(str(binarytree), '[[[0], 1, [2]], 3, [[4], 5, [6]]]')

if __name__ == '__main__':
    unittest.main(verbosity=2)
