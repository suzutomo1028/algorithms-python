#!/usr/bin/env python3

from __future__ import annotations
from typing import Any, Optional, Iterable
import sys, os
sys.path.append(os.pardir)
from algorithms import Element

class LinkedList:

    #--------------------------------------------------------------------------
    def __init__(self) -> None:
        self._len: int = 0
        self._head: Optional[Element] = None
        self._tail: Optional[Element] = None

    #--------------------------------------------------------------------------
    def __len__(self) -> int:
        return self._len

    #--------------------------------------------------------------------------
    def append(self, value: Any) -> None:
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
    def _element_at(self, index: int) -> Element:
        if index < 0 or self._len <= index:
            raise IndexError
        elem = self._head
        for _ in range(index):
            elem = elem.child
        return elem

    #--------------------------------------------------------------------------
    def insert(self, value: Any, index: int) -> None:
        new_elem = Element(value)
        elem = self._element_at(index)
        if elem.parent is None:
            new_elem.child = elem
            elem.parent = new_elem
            self._head = new_elem
        else:
            elem.parent.child = new_elem
            new_elem.parent = elem.parent
            new_elem.child = elem
            elem.parent = new_elem
        self._len += 1

    #--------------------------------------------------------------------------
    def remove(self, index: int) -> None:
        elem = self._element_at(index)
        if elem.parent is None:
            if elem.child is None:
                self._head = None
                self._tail = None
            else:
                elem.child.parent = None
                self._head = elem.child
        else:
            if elem.child is None:
                elem.parent.child = None
                self._tail = elem.parent
            else:
                elem.parent.child = elem.child
                elem.child.parent = elem.parent
        self._len -= 1

    #--------------------------------------------------------------------------
    def __getitem__(self, index: int) -> Any:
        return self._element_at(index).value

    #--------------------------------------------------------------------------
    def __setitem__(self, index: int, value: Any) -> None:
        self._element_at(index).value = value

    #--------------------------------------------------------------------------
    def clear(self) -> None:
        self._len = 0
        self._head = None
        self._tail = None

    #--------------------------------------------------------------------------
    @classmethod
    def from_iter(cls, itr: Iterable) -> LinkedList:
        if not isinstance(itr, Iterable):
            raise TypeError
        lnklst = cls()
        for value in itr:
            lnklst.append(value)
        return lnklst

    #--------------------------------------------------------------------------
    def to_list(self) -> list:
        lst = []
        elem = self._head
        while elem is not None:
            lst.append(elem.value)
            elem = elem.child
        return lst

    #--------------------------------------------------------------------------
    def clone(self) -> LinkedList:
        return LinkedList.from_iter(self.to_list())

    #--------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"LinkedList({self.to_list()})"
