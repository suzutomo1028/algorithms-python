#!/usr/bin/env python3

import sys, os
sys.path.append(os.pardir)
from algorithms import Queue
import pytest

class Test_Queue:

    #--------------------------------------------------------------------------
    def test_init(self) -> None:
        queue = Queue()
        assert queue._len == 0
        assert queue._head is None
        assert queue._tail is None

    #--------------------------------------------------------------------------
    def test_len(self) -> None:
        queue = Queue()
        assert len(queue) == 0

        queue.enqueue(1)
        assert len(queue) == 1

        queue.dequeue()
        assert len(queue) == 0

    #--------------------------------------------------------------------------
    def test_enqueue(self) -> None:
        queue = Queue()
        assert queue.to_list() == []

        queue.enqueue(1)
        assert queue.to_list() == [1]

        queue.enqueue(2)
        assert queue.to_list() == [1, 2]

    #--------------------------------------------------------------------------
    def test_dequeue(self) -> None:
        queue = Queue.from_iter([1, 2])
        assert queue.to_list() == [1, 2]

        assert queue.dequeue() == 1
        assert queue.to_list() == [2]

        assert queue.dequeue() == 2
        assert queue.to_list() == []

        with pytest.raises(RuntimeError):
            queue.dequeue()

    #--------------------------------------------------------------------------
    def test_peek(self) -> None:
        queue = Queue()
        with pytest.raises(RuntimeError):
            queue.peek()

        queue.enqueue(1)
        assert queue.peek() == 1

        queue.enqueue(2)
        assert queue.peek() == 1

        queue.dequeue()
        assert queue.peek() == 2

        queue.dequeue()
        with pytest.raises(RuntimeError):
            queue.peek()

    #--------------------------------------------------------------------------
    def test_clear(self) -> None:
        queue = Queue.from_iter([1, 2])
        assert queue.to_list() == [1, 2]

        queue.clear()
        assert queue.to_list() == []

    #--------------------------------------------------------------------------
    def test_from_iter(self) -> None:
        queue = Queue.from_iter([])
        assert queue.to_list() == []

        queue = Queue.from_iter([1, 2])
        assert queue.to_list() == [1, 2]

        queue = Queue.from_iter('hello')
        assert queue.to_list() == ['h', 'e', 'l', 'l', 'o']

        with pytest.raises(TypeError):
            Queue.from_iter(100)

    #--------------------------------------------------------------------------
    def test_to_list(self) -> None:
        queue = Queue()
        assert queue.to_list() == []

        queue = Queue.from_iter([1, 2])
        assert queue.to_list() == [1, 2]

        queue = Queue.from_iter('hello')
        assert queue.to_list() == ['h', 'e', 'l', 'l', 'o']

    #--------------------------------------------------------------------------
    def test_clone(self) -> None:
        queue = Queue()
        clone = queue.clone()
        assert clone is not queue
        assert clone.to_list() == queue.to_list()

        queue = Queue.from_iter([1, 2])
        clone = queue.clone()
        assert clone is not queue
        assert clone.to_list() == queue.to_list()

        queue = Queue.from_iter('hello')
        clone = queue.clone()
        assert clone is not queue
        assert clone.to_list() == queue.to_list()

    #--------------------------------------------------------------------------
    def test_str(self) -> None:
        queue = Queue()
        assert str(queue) == "Queue([])"

        queue = Queue.from_iter([1, 2])
        assert str(queue) == "Queue([1, 2])"

        queue = Queue.from_iter('hello')
        assert str(queue) == "Queue(['h', 'e', 'l', 'l', 'o'])"
