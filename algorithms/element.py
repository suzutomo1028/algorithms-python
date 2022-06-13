#!/usr/bin/env python3

from typing import Any

class Element:
    """ 要素 """

    def __init__(self, value: Any) -> None:
        """ インスタンスを初期化する
        """
        self.value: Any = value
        self.parent: Element = None
        self.child: Element = None

    def __str__(self) -> str:
        """ 要素の文字列表現を返す
        """
        return str(self.value)

if __name__ == '__main__':
    pass
