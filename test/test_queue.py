#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
from algorithms import Queue

class Test_Queue(unittest.TestCase):

    def test_init(self) -> None:
        queue = Queue()
        self.assertEqual(queue.count, 0)
        self.assertEqual(queue.is_empty, True)
        self.assertListEqual(queue.to_list(), [])

    def test_enqueue(self) -> None:
        queue = Queue()

        queue.enqueue(0)
        self.assertEqual(queue.count, 1)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [0])

        queue.enqueue(1)
        self.assertEqual(queue.count, 2)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [0, 1])

        queue.enqueue(2)
        self.assertEqual(queue.count, 3)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [0, 1, 2])

    def test_bulk_enqueue(self) -> None:
        queue = Queue()

        queue.bulk_enqueue([0, 1, 2])
        self.assertEqual(queue.count, 3)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [0, 1, 2])

        queue.bulk_enqueue([3, 4, 5])
        self.assertEqual(queue.count, 6)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [0, 1, 2, 3, 4, 5])

        with self.assertRaises(TypeError):
            queue.bulk_enqueue(6)

    def test_dequeue(self) -> None:
        queue = Queue()
        queue.bulk_enqueue([0, 1, 2])

        value = queue.dequeue()
        self.assertEqual(value, 0)
        self.assertEqual(queue.count, 2)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [1, 2])

        value = queue.dequeue()
        self.assertEqual(value, 1)
        self.assertEqual(queue.count, 1)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [2])

        value = queue.dequeue()
        self.assertEqual(value, 2)
        self.assertEqual(queue.count, 0)
        self.assertEqual(queue.is_empty, True)
        self.assertListEqual(queue.to_list(), [])

        with self.assertRaises(RuntimeError):
            value = queue.dequeue()

    def test_bulk_dequeue(self) -> None:
        queue = Queue()
        queue.bulk_enqueue([0, 1, 2, 3, 4, 5])

        lst = queue.bulk_dequeue(0)
        self.assertListEqual(lst, [])
        self.assertEqual(queue.count, 6)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [0, 1, 2, 3, 4, 5])

        lst = queue.bulk_dequeue(3)
        self.assertListEqual(lst, [0, 1, 2])
        self.assertEqual(queue.count, 3)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [3, 4, 5])

        lst = queue.bulk_dequeue(3)
        self.assertListEqual(lst, [3, 4, 5])
        self.assertEqual(queue.count, 0)
        self.assertEqual(queue.is_empty, True)
        self.assertListEqual(queue.to_list(), [])

        with self.assertRaises(ValueError):
            lst = queue.bulk_dequeue(-1)

        with self.assertRaises(ValueError):
            lst = queue.bulk_dequeue(1)

    def test_clear(self) -> None:
        queue = Queue()
        queue.bulk_enqueue([0, 1, 2])

        queue.clear()
        self.assertEqual(queue.count, 0)
        self.assertEqual(queue.is_empty, True)
        self.assertListEqual(queue.to_list(), [])

    def test_peek(self) -> None:
        queue = Queue()
        queue.bulk_enqueue([0, 1, 2])

        value = queue.peek()
        self.assertEqual(value, 0)

        queue.dequeue()

        value = queue.peek()
        self.assertEqual(value, 1)

        queue.dequeue()

        value = queue.peek()
        self.assertEqual(value, 2)

        queue.dequeue()

        with self.assertRaises(RuntimeError):
            value = queue.peek()

    def test_from_iterable(self) -> None:
        queue = Queue.from_iterable([0, 1, 2])
        self.assertEqual(queue.count, 3)
        self.assertEqual(queue.is_empty, False)
        self.assertListEqual(queue.to_list(), [0, 1, 2])

        with self.assertRaises(TypeError):
            queue = Queue.from_iterable(0)

    def test_to_list(self) -> None:
        queue = Queue.from_iterable([0, 1, 2])

        self.assertListEqual(queue.to_list(), [0, 1, 2])

    def test_clone(self) -> None:
        queue_a = Queue.from_iterable([0, 1, 2])

        queue_b = queue_a.clone()
        self.assertIsNot(queue_b, queue_a)
        self.assertListEqual(queue_b.to_list(), queue_a.to_list())

    def test_str(self) -> None:
        queue = Queue.from_iterable([0, 1, 2])

        self.assertEqual(str(queue), '[0, 1, 2]')

if __name__ == '__main__':
    unittest.main(verbosity=2)
