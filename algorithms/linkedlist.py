#!/usr/bin/env python3

from __future__ import annotations
import sys, os
from typing import Any, Iterable, Iterator

sys.path.append(os.pardir)
from algorithms import Element

class LinkedList:
    """ 連結リスト """

    def __init__(self) -> None:
        """ インスタンスを初期化する
        """
        self.__head: Element = None
        self.__tail: Element = None
        self.__count: int = 0
        self.__index: int = 0

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

    def append(self, value: Any) -> None:
        """ 末尾に要素を追加する
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

    def bulk_append(self, iter: Iterable) -> None:
        """ 末尾に複数の要素を追加する
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        for value in iter:
            self.append(value)

    def __element_at(self, index: int) -> Element:
        if (index < 0) or (self.__count <= index):
            raise IndexError

        elem = self.__head
        for _ in range(index):
            elem = elem.child
        return elem

    def insert(self, index: int, value: Any) -> None:
        """ 指定位置に要素を挿入する
        """
        if (index < 0) or (self.__count <= index):
            raise IndexError

        elem = self.__element_at(index)
        new_elem = Element(value)
        if elem.parent is None:
            new_elem.child = self.__head
            new_elem.child.parent = new_elem
            self.__head = new_elem
        else:
            new_elem.parent = elem.parent
            new_elem.parent.child = new_elem
            new_elem.child = elem
            new_elem.child.parent = new_elem
        self.__count += 1

    def bulk_insert(self, index: int, iter: Iterable) -> None:
        """ 指定位置に複数の要素を挿入する
        """
        if (index < 0) or (self.__count <= index):
            raise IndexError
        if not isinstance(iter, Iterable):
            raise TypeError

        for offset, value in enumerate(iter):
            self.insert(index + offset, value)

    def remove(self, index: int) -> None:
        """ 指定位置の要素を削除する
        """
        if (index < 0) or (self.__count <= index):
            raise IndexError

        elem = self.__element_at(index)
        if elem.parent is None:
            if elem.child is None:
                self.__head = None
                self.__tail = None
            else:
                elem.child.parent = None
                self.__head = elem.child
        else:
            if elem.child is None:
                elem.parent.child = None
                self.__tail = elem.parent
            else:
                elem.parent.child = elem.child
                elem.child.parent = elem.parent
        self.__count -= 1

    def bulk_remove(self, index: int, count: int) -> None:
        """ 指定位置から複数の要素を削除する
        """
        if (index < 0) or (self.__count <= index):
            raise IndexError
        if (count < 0) or (self.__count - index < count):
            raise ValueError

        for _ in range(count):
            self.remove(index)

    def clear(self) -> None:
        """ 全ての要素を削除する
        """
        self.__head = None
        self.__tail = None
        self.__count = 0
        self.__index = 0

    def __add__(self, iter: Iterable) -> LinkedList:
        """ 左辺の連結リストの末尾に右辺の連結リストを追加した、新たな連結リストを返す
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        linkedlist = self.clone()
        linkedlist.bulk_append(iter)
        return linkedlist

    def __iadd__(self, iter: Iterable) -> LinkedList:
        """ 左辺の連結リストの末尾に右辺の連結リストを追加して、左辺の連結リストを返す
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        self.bulk_append(iter)
        return self

    def __getitem__(self, index: int) -> Any:
        """ 指定位置の要素を返す
        """
        if (index < 0) or (self.__count <= index):
            raise IndexError

        elem = self.__element_at(index)
        return elem.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ 指定位置の要素を設定する
        """
        if (index < 0) or (self.__count <= index):
            raise IndexError

        elem = self.__element_at(index)
        elem.value = value

    def __next__(self) -> Any:
        """ イテレータ機能において次の要素を返す
        """
        try:
            value = self[self.__index]
        except IndexError:
            raise StopIteration
        self.__index += 1
        return value

    def __iter__(self) -> Iterator:
        """ イテレータオブジェクトとして自身を返す
        """
        self.__index = 0
        return self

    @classmethod
    def from_iterable(cls, iter: Iterable) -> LinkedList:
        """ イテラブルオブジェクトと同じ要素を持つ連結リストを返す
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        linkedlist = LinkedList()
        for value in iter:
            linkedlist.append(value)
        return linkedlist

    def to_list(self) -> list:
        """ 連結リストと同じ要素を持つリストを返す
        """
        lst = []
        for i in range(self.__count):
            lst.append(self[i])
        return lst

    def clone(self) -> LinkedList:
        """ 連結リストと同じ要素を持つ新たな連結リストを返す
        """
        lst = self.to_list()
        return LinkedList.from_iterable(lst)

    def get_range(self, index: int, count: int) -> LinkedList:
        """ 指定位置から指定数の要素を持つ新たな連結リストを返す
        """
        if (index < 0) or (self.__count <= index):
            raise IndexError
        if (count < 0) or (self.__count - index < count):
            raise ValueError

        linkedlist = LinkedList()
        for i in range(count):
            linkedlist.append(self[index + i])
        return linkedlist

    def __str__(self) -> str:
        """ 連結リストの文字列表現を返す
        """
        return str(self.to_list())

    def sort(self) -> None:
        """ 要素を昇順に並べ替える
        """
        if self.__count <= 1:
            return
        pivot = self[0]
        left, middle, right = LinkedList(), LinkedList(), LinkedList()
        elem = self.__head
        while elem is not None:
            if elem.value == pivot:
                middle.append(elem.value)
            elif elem.value < pivot:
                left.append(elem.value)
            else:
                right.append(elem.value)
            elem = elem.child
        left.sort()
        right.sort()
        self.clear()
        self += left + middle + right

if __name__ == '__main__':
    pass
