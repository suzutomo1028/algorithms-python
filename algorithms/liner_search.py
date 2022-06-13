#!/usr/bin/env python3

from typing import Any

def liner_search(arr: list, key: Any) -> int:
    """ 線形探索
    """
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return None

if __name__ == '__main__':
    pass
