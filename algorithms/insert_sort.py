#!/usr/bin/env python3

def insert_sort(arr: list) -> list:
    """ 挿入ソート
    """
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i - 1
        while (elem < arr[j]) and (0 <= j):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr

if __name__ == '__main__':
    pass
