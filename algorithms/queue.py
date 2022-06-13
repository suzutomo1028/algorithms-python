#!/usr/bin/env python3

from __future__ import annotations
import sys, os
from typing import Any, Iterable

sys.path.append(os.pardir)
from algorithms import Element

class Queue:
    """ キュー """

    def __init__(self) -> None:
        """ インスタンスを初期化する
        """
        self.__head: Element = None
        self.__tail: Element = None
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

    def enqueue(self, value: Any) -> None:
        """ 末尾に要素を挿入する
        """
        new_elem = Element(value)
        if self.is_empty:
            self.__head = new_elem
            self.__tail = new_elem
        else:
            new_elem.parent = self.__tail
            new_elem.parent.child = new_elem
            self.__tail = new_elem
        self.__count += 1

    def bulk_enqueue(self, iter: Iterable) -> None:
        """ 末尾に複数の要素を挿入する
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        for value in iter:
            self.enqueue(value)

    def dequeue(self) -> Any:
        """ 先頭の要素を削除して、その要素を返す
        """
        if self.is_empty:
            raise RuntimeError

        elem = self.__head
        if elem.child is None:
            self.__head = None
            self.__tail = None
        else:
            elem.child.parent = None
            self.__head = elem.child
        self.__count -= 1
        return elem.value

    def bulk_dequeue(self, count: int) -> list:
        """ 先頭から複数の要素を削除して、それら要素のリストを返す
        """
        if (count < 0) or (self.__count < count):
            raise ValueError

        lst = []
        for _ in range(count):
            lst.append(self.dequeue())
        return lst

    def clear(self) -> None:
        """ 全ての要素を削除する
        """
        self.__head = None
        self.__tail = None
        self.__count = 0

    def peek(self) -> Any:
        """ 先頭要素の値を返す
        """
        if self.is_empty:
            raise RuntimeError

        return self.__head.value

    @classmethod
    def from_iterable(cls, iter: Iterable) -> Queue:
        """ イテラブルオブジェクトと同じ要素を持つキューを返す
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        queue = Queue()
        for value in iter:
            queue.enqueue(value)
        return queue

    def to_list(self) -> list:
        """ キューと同じ要素を持つリストを返す
        """
        lst = []
        elem = self.__head
        while elem is not None:
            lst.append(elem.value)
            elem = elem.child
        return lst

    def clone(self) -> Queue:
        """ キューと同じ要素を持つ新たなキューを返す
        """
        lst = self.to_list()
        return Queue.from_iterable(lst)

    def __str__(self) -> str:
        """ キューの文字列表現を返す
        """
        return str(self.to_list())

if __name__ == '__main__':
    pass
