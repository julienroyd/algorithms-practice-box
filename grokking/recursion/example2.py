# Comparing using a loop and using recursion

def traditional_sum(array):
    total = 0
    for x in array:
        total += x
    return total

def recursive_sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + recursive_sum(array[1:])

def recursive_count(array):
    if len(array) == 0:
        return 0
    else:
        return 1 + recursive_count(array[1:])

def recursive_max(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    else:
        tmp_max = recursive_max(array[1:])
        return array[0] if array[0] > tmp_max else tmp_max


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 60, 7, 8]
    print(f"total={traditional_sum(array)}")
    print(f"total={recursive_sum(array)}")
    print(f"count={recursive_count(array)}")
    print(f"max={recursive_max(array)}")
