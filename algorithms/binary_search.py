#!/usr/bin/env python3

from typing import Any

def binary_search(arr: list, key: Any) -> int:
    """ 二分探索
    """
    left_index = 0
    right_index = len(arr) - 1
    while left_index <= right_index:
        pivot_index = (left_index + right_index) // 2
        pivot = arr[pivot_index]
        if key == pivot:
            return pivot_index
        elif key < pivot:
            right_index = pivot_index - 1
        else:
            left_index = pivot_index + 1
    return None

if __name__ == '__main__':
    pass
