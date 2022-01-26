# Simple implementation of quicksort: O(log n)

from copy import deepcopy
import random

COUNT = 0

first_pivot = lambda arr: 0
half_pivot = lambda arr: len(arr) // 2

def quicksort(array, pivot_fn):
    global COUNT
    COUNT = COUNT + 1

    if len(array) < 2:
        return array

    elif len(array) == 2:
        return array if array[0] < array[1] else array[::-1]

    else:
        pivot_idx = pivot_fn(array)
        pivot = array.pop(pivot_idx)
        left_array = [x for x in array if x <= pivot]
        right_array = [x for x in array if x > pivot]
        return quicksort(left_array, pivot_fn) + [pivot] + quicksort(right_array, pivot_fn)


if __name__ == '__main__':
    init_array = list(range(20))
    random.shuffle(init_array)
    for pivot_fn in [first_pivot, half_pivot]:
        for array in (list(sorted(deepcopy(init_array))), deepcopy(init_array), list(sorted(deepcopy(init_array), reverse=True))):
            COUNT = 0
            print(f"\n\n-----------------------\narray={array}")
            print(f"sorted={quicksort(array, pivot_fn=pivot_fn)}, COUNT={COUNT}")
