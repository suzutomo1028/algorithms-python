#!/usr/bin/env python3

def quick_sort(arr: list) -> list:
    """ クイックソート
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, middle, right = [], [], []
    for elem in arr:
        if elem == pivot:
            middle.append(elem)
        elif elem < pivot:
            left.append(elem)
        else:
            right.append(elem)
    left = quick_sort(left)
    right = quick_sort(right)
    arr = left + middle + right
    return arr

if __name__ == '__main__':
    pass
