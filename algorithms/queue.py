#!/usr/bin/env python3

from __future__ import annotations
from typing import Any, Optional, Iterable
import sys, os
sys.path.append(os.pardir)
from algorithms import Element

class Queue:

    #--------------------------------------------------------------------------
    def __init__(self) -> None:
        self._len: int = 0
        self._head: Optional[Element] = None
        self._tail: Optional[Element] = None

    #--------------------------------------------------------------------------
    def __len__(self) -> int:
        return self._len

    #--------------------------------------------------------------------------
    def enqueue(self, value: Any) -> None:
        new_elem = Element(value)
        if self._tail is None:
            self._head = new_elem
            self._tail = new_elem
        else:
            self._tail.child = new_elem
            new_elem.parent = self._tail
            self._tail = new_elem
        self._len += 1

    #--------------------------------------------------------------------------
    def dequeue(self) -> Any:
        if self._head is None:
            raise RuntimeError
        value = self._head.value
        if self._head.child is None:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.child
            self._head.parent = None
        self._len -= 1
        return value

    #--------------------------------------------------------------------------
    def peek(self) -> Any:
        if self._head is None:
            raise RuntimeError
        return self._head.value

    #--------------------------------------------------------------------------
    def clear(self) -> None:
        self._len = 0
        self._head = None
        self._tail = None

    #--------------------------------------------------------------------------
    @classmethod
    def from_iter(cls, itr: Iterable) -> Queue:
        if not isinstance(itr, Iterable):
            raise TypeError
        queue = cls()
        for value in itr:
            queue.enqueue(value)
        return queue

    def to_list(self) -> list:
        lst = []
        elem = self._head
        while elem is not None:
            lst.append(elem.value)
            elem = elem.child
        return lst

    #--------------------------------------------------------------------------
    def clone(self) -> Queue:
        return Queue.from_iter(self.to_list())

    #--------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"Queue({self.to_list()})"
