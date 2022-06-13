#!/usr/bin/env python3

def bubble_sort(arr: list) -> list:
    """ バブルソート
    """
    while True:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == '__main__':
    pass
