import random
import time
from copy import deepcopy

def binary_search(sorted_array, target):
    print(f"\nTarget={target}")
    low_i = 0
    high_i = len(sorted_array) - 1
    step = 0

    while True:
        step += 1
        time.sleep(0.3)

        if low_i == high_i:
            print(f"{target} not in the array.")
            return
        else:
            guess_i = (high_i + low_i) // 2

            if sorted_array[guess_i] == target:
                print(f"{step} - Found: i={guess_i}")
                return guess_i

            elif sorted_array[guess_i] < target:
                low_i = deepcopy(guess_i) + 1
                print(f"{step} - guess={guess_i}. Too low: range=[{low_i}, {high_i}]")

            elif sorted_array[guess_i] > target:
                high_i = deepcopy(guess_i)
                print(f"{step} - guess={guess_i}. Too high: range=[{low_i}, {high_i}]")

            else:
                raise ValueError()

if __name__ == '__main__':
    binary_search(list(range(1000000)), random.randint(0, 1000000))
    binary_search(list(range(1000000)), -1)
