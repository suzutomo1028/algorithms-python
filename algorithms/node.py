#!/usr/bin/env python3

from typing import Any

class Node:
    """ 節点 """

    def __init__(self, value: Any) -> None:
        """ インスタンスを初期化する
        """
        self.value: Any = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self) -> str:
        """ 節点の文字列表現を返す
        """
        return str(self.value)

if __name__ == '__main__':
    pass
