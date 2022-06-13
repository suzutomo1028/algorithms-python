#!/usr/bin/env python3

def merge(left: list, right: list) -> list:
    """ 2つのリストを統合する
    """
    arr = []
    i, j = 0, 0
    while (i < len(left)) and(j < len(right)):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    if i < len(left):
        arr.extend(left[i:])
    if j < len(right):
        arr.extend(right[j:])
    return arr

def merge_sort(arr: list) -> list:
    """ マージソート
    """
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    arr = merge(left, right)
    return arr

if __name__ == '__main__':
    pass
