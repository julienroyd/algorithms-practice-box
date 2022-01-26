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


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"total={traditional_sum(array)}")
    print(f"total={recursive_sum(array)}")
