#!/usr/bin/env python3

def select_sort(arr: list) ->list:
    """ 選択ソート
    """
    for i in range(len(arr)):
        j = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    pass
