#!/usr/bin/env python3

from __future__ import annotations
from typing import Any, Optional, Iterable
import sys, os
sys.path.append(os.pardir)
from algorithms import Element

class Stack:

    #--------------------------------------------------------------------------
    def __init__(self) -> None:
        self._len: int = 0
        self._top: Optional[Element] = None

    #--------------------------------------------------------------------------
    def __len__(self) -> int:
        return self._len

    #--------------------------------------------------------------------------
    def push(self, value: Any) -> None:
        new_elem = Element(value)
        if self._top is None:
            self._top = new_elem
        else:
            new_elem.child = self._top
            self._top.parent = new_elem
            self._top = new_elem
        self._len += 1

    #--------------------------------------------------------------------------
    def pop(self) -> Any:
        if self._top is None:
            raise RuntimeError
        value = self._top.value
        if self._top.child is None:
            self._top = None
        else:
            self._top = self._top.child
            self._top.parent = None
        self._len -= 1
        return value

    #--------------------------------------------------------------------------
    def peek(self) -> Any:
        if self._top is None:
            raise RuntimeError
        return self._top.value

    #--------------------------------------------------------------------------
    def clear(self) -> None:
        self._len = 0
        self._top = None

    #--------------------------------------------------------------------------
    @classmethod
    def from_iter(cls, itr: Iterable) -> Stack:
        if not isinstance(itr, Iterable):
            raise TypeError
        stack = cls()
        for value in itr:
            stack.push(value)
        return stack

    #--------------------------------------------------------------------------
    def to_list(self) -> list:
        lst = []
        elem = self._top
        while elem is not None:
            lst.append(elem.value)
            elem = elem.child
        return lst

    #--------------------------------------------------------------------------
    def clone(self) -> Stack:
        return Stack.from_iter(self.to_list()[::-1])

    #--------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"Stack({self.to_list()})"
