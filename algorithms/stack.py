#!/usr/bin/env python3

from __future__ import annotations
import sys, os
from typing import Any, Iterable

sys.path.append(os.pardir)
from algorithms import Element

class Stack:
    """ スタック """

    def __init__(self) -> None:
        """ インスタンスを初期化する
        """
        self.__top: Element = None
        self.__count: int = 0

    @property
    def count(self) -> int:
        """ 要素数を返す
        """
        return self.__count

    @property
    def is_empty(self) -> bool:
        """ 要素数が 0 のとき True を返す
        """
        return bool(self.__count == 0)

    def push(self, value: Any) -> None:
        """ 頂上に要素を挿入する
        """
        new_elem = Element(value)
        if self.is_empty:
            self.__top = new_elem
        else:
            new_elem.child = self.__top
            new_elem.child.parent = new_elem
            self.__top = new_elem
        self.__count += 1

    def bulk_push(self, iter: Iterable) -> None:
        """ 頂上に複数の要素を挿入する
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        for value in iter:
            self.push(value)

    def pop(self) -> Any:
        """ 頂上の要素を削除して、その要素を返す
        """
        if self.is_empty:
            raise RuntimeError

        elem = self.__top
        if elem.child is None:
            self.__top = None
        else:
            elem.child.parent = None
            self.__top = elem.child
        self.__count -= 1
        return elem.value

    def bulk_pop(self, count: int) -> list:
        """ 頂上から複数の要素を削除して、それら要素のリストを返す
        """
        if (count < 0) or (self.__count < count):
            raise ValueError

        lst = []
        for _ in range(count):
            lst.append(self.pop())
        return lst

    def clear(self) -> None:
        """ 全ての要素を削除する
        """
        self.__top = None
        self.__count = 0

    def peek(self) -> Any:
        """ 頂上要素の値を返す
        """
        if self.is_empty:
            raise RuntimeError

        return self.__top.value

    @classmethod
    def from_iterable(cls, iter: Iterable) -> Stack:
        """ イテラブルオブジェクトと同じ要素を持つスタックを返す
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        stack = Stack()
        for value in iter:
            stack.push(value)
        return stack

    def to_list(self) -> list:
        """ スタックと同じ要素を持つリストを返す
        """
        lst = []
        elem = self.__top
        while elem is not None:
            lst.append(elem.value)
            elem = elem.child
        return lst

    def clone(self) -> Stack:
        """ スタックと同じ要素を持つ新たなスタックを返す
        """
        lst = self.to_list()
        lst.reverse()
        return Stack.from_iterable(lst)

    def __str__(self) -> str:
        """ スタックの文字列表現を返す
        """
        return str(self.to_list())

if __name__ == '__main__':
    pass
