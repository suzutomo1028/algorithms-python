#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
from algorithms import Stack

class Test_Stack(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack()
        self.assertEqual(stack.count, 0)
        self.assertEqual(stack.is_empty, True)
        self.assertListEqual(stack.to_list(), [])

    def test_push(self) -> None:
        stack = Stack()

        stack.push(0)
        self.assertEqual(stack.count, 1)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [0])

        stack.push(1)
        self.assertEqual(stack.count, 2)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [1, 0])

        stack.push(2)
        self.assertEqual(stack.count, 3)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [2, 1, 0])

    def test_bulk_push(self) -> None:
        stack = Stack()

        stack.bulk_push([0, 1, 2])
        self.assertEqual(stack.count, 3)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [2, 1, 0])

        stack.bulk_push([3, 4, 5])
        self.assertEqual(stack.count, 6)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [5, 4, 3, 2, 1, 0])

        with self.assertRaises(TypeError):
            stack.bulk_push(6)

    def test_pop(self) -> None:
        stack = Stack()
        stack.bulk_push([0, 1, 2])

        value = stack.pop()
        self.assertEqual(value, 2)
        self.assertEqual(stack.count, 2)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [1, 0])

        value = stack.pop()
        self.assertEqual(value, 1)
        self.assertEqual(stack.count, 1)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [0])

        value = stack.pop()
        self.assertEqual(value, 0)
        self.assertEqual(stack.count, 0)
        self.assertEqual(stack.is_empty, True)
        self.assertListEqual(stack.to_list(), [])

        with self.assertRaises(RuntimeError):
            value = stack.pop()

    def test_bulk_pop(self) -> None:
        stack = Stack()
        stack.bulk_push([0, 1, 2, 3, 4, 5])

        lst = stack.bulk_pop(0)
        self.assertListEqual(lst, [])
        self.assertEqual(stack.count, 6)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [5, 4, 3, 2, 1, 0])

        lst = stack.bulk_pop(3)
        self.assertListEqual(lst, [5, 4, 3])
        self.assertEqual(stack.count, 3)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [2, 1, 0])

        lst = stack.bulk_pop(3)
        self.assertListEqual(lst, [2, 1, 0])
        self.assertEqual(stack.count, 0)
        self.assertEqual(stack.is_empty, True)
        self.assertListEqual(stack.to_list(), [])

        with self.assertRaises(ValueError):
            lst = stack.bulk_pop(-1)

        with self.assertRaises(ValueError):
            lst = stack.bulk_pop(1)

    def test_clear(self) -> None:
        stack = Stack()
        stack.bulk_push([0, 1, 2])

        stack.clear()
        self.assertEqual(stack.count, 0)
        self.assertEqual(stack.is_empty, True)
        self.assertListEqual(stack.to_list(), [])

    def test_peek(self) -> None:
        stack = Stack()
        stack.bulk_push([0, 1, 2])

        value = stack.peek()
        self.assertEqual(value, 2)

        stack.pop()

        value = stack.peek()
        self.assertEqual(value, 1)

        stack.pop()

        value = stack.peek()
        self.assertEqual(value, 0)

        stack.pop()

        with self.assertRaises(RuntimeError):
            value = stack.peek()

    def test_from_iterable(self) -> None:
        stack = Stack.from_iterable([0, 1, 2])
        self.assertEqual(stack.count, 3)
        self.assertEqual(stack.is_empty, False)
        self.assertListEqual(stack.to_list(), [2, 1, 0])

        with self.assertRaises(TypeError):
            stack = Stack.from_iterable(0)

    def test_to_list(self) -> None:
        stack = Stack.from_iterable([0, 1, 2])

        self.assertListEqual(stack.to_list(), [2, 1, 0])

    def test_clone(self) -> None:
        stack_a = Stack.from_iterable([0, 1, 2])

        stack_b = stack_a.clone()
        self.assertIsNot(stack_b, stack_a)
        self.assertListEqual(stack_b.to_list(), stack_a.to_list())

    def test_str(self) -> None:
        stack = Stack.from_iterable([0, 1, 2])

        self.assertEqual(str(stack), '[2, 1, 0]')

if __name__ == '__main__':
    unittest.main(verbosity=2)
