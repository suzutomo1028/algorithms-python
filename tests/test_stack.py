#!/usr/bin/env python3

import sys, os
sys.path.append(os.pardir)
from algorithms import Stack
import pytest

class Test_Stack:

    #--------------------------------------------------------------------------
    def test_init(self) -> None:
        stack = Stack()
        assert stack._len == 0
        assert stack._top == None

    #--------------------------------------------------------------------------
    def test_len(self) -> None:
        stack = Stack()
        assert len(stack) == 0

        stack.push(1)
        assert len(stack) == 1

        stack.pop()
        assert len(stack) == 0

    #--------------------------------------------------------------------------
    def test_push(self) -> None:
        stack = Stack()
        assert stack.to_list() == []

        stack.push(1)
        assert stack.to_list() == [1]

        stack.push(2)
        assert stack.to_list() == [2, 1]

    #--------------------------------------------------------------------------
    def test_pop(self) -> None:
        stack = Stack.from_iter([1, 2])
        assert stack.to_list() == [2, 1]

        assert stack.pop() == 2
        assert stack.to_list() == [1]

        assert stack.pop() == 1
        assert stack.to_list() == []

        with pytest.raises(RuntimeError):
            stack.pop()

    #--------------------------------------------------------------------------
    def test_peek(self) -> None:
        stack = Stack()
        with pytest.raises(RuntimeError):
            stack.peek()

        stack.push(1)
        assert stack.peek() == 1

        stack.push(2)
        assert stack.peek() == 2

        stack.pop()
        assert stack.peek() == 1

        stack.pop()
        with pytest.raises(RuntimeError):
            stack.peek()

    #--------------------------------------------------------------------------
    def test_clear(self) -> None:
        stack = Stack.from_iter([1, 2])
        assert stack.to_list() == [2, 1]

        stack.clear()
        assert stack.to_list() == []

    #--------------------------------------------------------------------------
    def test_from_iter(self) -> None:
        stack = Stack.from_iter([])
        assert stack.to_list() == []

        stack = Stack.from_iter([1, 2])
        assert stack.to_list() == [2, 1]

        stack = Stack.from_iter('hello')
        assert stack.to_list() == ['o', 'l', 'l', 'e', 'h']

        with pytest.raises(TypeError):
            Stack.from_iter(100)

    #--------------------------------------------------------------------------
    def test_to_list(self) -> None:
        stack = Stack()
        assert stack.to_list() == []

        stack = Stack.from_iter([1, 2])
        assert stack.to_list() == [2, 1]

        stack = Stack.from_iter('hello')
        assert stack.to_list() == ['o', 'l', 'l', 'e', 'h']

    #--------------------------------------------------------------------------
    def test_clone(self) -> None:
        stack = Stack()
        clone = stack.clone()
        assert clone is not stack
        assert clone.to_list() == stack.to_list()

        stack = Stack.from_iter([1, 2])
        clone = stack.clone()
        assert clone is not stack
        assert clone.to_list() == stack.to_list()

        stack = Stack.from_iter('hello')
        clone = stack.clone()
        assert clone is not stack
        assert clone.to_list() == stack.to_list()

    #--------------------------------------------------------------------------
    def test_str(self) -> None:
        stack = Stack()
        assert str(stack) == "Stack([])"

        stack = Stack.from_iter([1, 2])
        assert str(stack) == "Stack([2, 1])"

        stack = Stack.from_iter('hello')
        assert str(stack) == "Stack(['o', 'l', 'l', 'e', 'h'])"
