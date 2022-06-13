#!/usr/bin/env python3

from __future__ import annotations
import sys, os
from typing import Any, Iterable

sys.path.append(os.pardir)
from algorithms import Node

class BinaryTree:
    """ 二分木 """

    def __init__(self) -> None:
        """ インスタンスを初期化する
        """
        self.__root: Node = None
        self.__count: int = 0

    @property
    def count(self) -> int:
        """ 節点数を返す
        """
        return self.__count

    @property
    def is_empty(self) -> bool:
        """ 節点数が 0 のとき True を返す
        """
        return bool(self.__count == 0)

    def __insert(self, node: Node, value: Any) -> None:
        if node is None:
            node = Node(value)
            self.__count += 1
        else:
            if value < node.value:
                node.left = self.__insert(node.left, value)
            else:
                node.right = self.__insert(node.right, value)
        return node

    def insert(self, value: Any) -> None:
        """ 節点を挿入する
        """
        self.__root = self.__insert(self.__root, value)

    def bulk_insert(self, iter: Iterable) -> None:
        """ 複数の節点を挿入する
        """
        if not isinstance(iter, Iterable):
            raise TypeError

        for value in iter:
            self.insert(value)

    def __min(self, node: Node) -> Node:
        if node is None:
            raise ValueError

        if node.left is not None:
            node = self.__min(node.left)
        return node

    def min(self) -> Any:
        """ 節点の最小値を返す
        """
        try:
            return self.__min(self.__root).value
        except ValueError:
            raise RuntimeError

    def __max(self, node: Node) -> Node:
        if node is None:
            raise ValueError

        if node.right is not None:
            node = self.__max(node.right)
        return node

    def max(self) -> Any:
        """ 節点の最大値を返す
        """
        try:
            return self.__max(self.__root).value
        except ValueError:
            raise RuntimeError

    def __remove_min(self, node: Node) -> Node:
        if node is None:
            raise ValueError

        if node.left is None:
            node = node.right
            self.__count -= 1
        else:
            node.left = self.__remove_min(node.left)
        return node

    def remove_min(self) -> None:
        """ 最小値の節点を削除する
        """
        try:
            self.__root = self.__remove_min(self.__root)
        except ValueError:
            raise RuntimeError

    def __remove_max(self, node: Node) -> Node:
        if node is None:
            raise ValueError

        if node.right is None:
            node = node.left
            self.__count -= 1
        else:
            node.right = self.__remove_max(node.right)
        return node

    def remove_max(self) -> None:
        """ 最大値の節点を削除する
        """
        try:
            self.__root = self.__remove_max(self.__root)
        except ValueError:
            raise RuntimeError

    def __remove(self, node: Node, value: Any) -> Node:
        if node is None:
            raise ValueError

        if value == node.value:
            if node.right is None:
                node = node.left
                self.__count -= 1
            else:
                value = self.__min(node.right).value
                node.right = self.__remove_min(node.right)
                node.value = value
        elif value < node.value:
            node.left = self.__remove(node.left, value)
        else:
            node.right = self.__remove(node.right, value)
        return node

    def remove(self, value: Any) -> None:
        """ 指定値の節点を削除する
        """
        try:
            self.__root = self.__remove(self.__root, value)
        except ValueError:
            raise RuntimeError

    def clear(self) -> None:
        """ 全ての節点を削除する
        """
        self.__root = None
        self.__count = 0

    def __depth(self, node: Node) -> int:
        if node is None:
            raise ValueError

        left_depth = 0
        if node.left is not None:
            left_depth = self.__depth(node.left) + 1
        right_depth = 0
        if node.right is not None:
            right_depth = self.__depth(node.right) + 1
        if left_depth < right_depth:
            depth = right_depth
        else:
            depth = left_depth
        return depth

    def depth(self) -> int:
        """ 深さを返す
        """
        try:
            return self.__depth(self.__root)
        except ValueError:
            raise RuntimeError

    @classmethod
    def from_iterable(cls, iter: Iterable) -> BinaryTree:
        """ イテラブルオブジェクトと同じ要素を持つ二分木を返す
        """
        binarytree = BinaryTree()
        for value in iter:
            binarytree.insert(value)
        return binarytree

    def __to_list(self, node: Node) -> list:
        lst = []
        if node is not None:
            if node.left is not None:
                lst.append(self.__to_list(node.left))
            lst.append(node.value)
            if node.right is not None:
                lst.append(self.__to_list(node.right))
        return lst

    def to_list(self) -> list:
        """ 二分木と同じ要素を持つリストを返す
        """
        return self.__to_list(self.__root)

    def __clone(self, node: Node, binarytree: BinaryTree) -> BinaryTree:
        if node is None:
            raise ValueError
        if binarytree is None:
            raise ValueError

        binarytree.insert(node.value)
        if node.left is not None:
            binarytree = self.__clone(node.left, binarytree)
        if node.right is not None:
            binarytree = self.__clone(node.right, binarytree)
        return binarytree

    def clone(self) -> BinaryTree:
        """ 二分木と同じ要素を持つ新たな二分木を返す
        """
        try:
            return self.__clone(self.__root, BinaryTree())
        except ValueError:
            raise RuntimeError

    def __str__(self) -> str:
        """ 二分木の文字列表現を返す
        """
        return str(self.to_list())

if __name__ == '__main__':
    pass
