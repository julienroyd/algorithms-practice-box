def find_smallest(items):
    smallest_item = items[0]
    smallest_idx = 0
    for i in range(1, len(items)):
        if items[i] <= smallest_item:
            smallest_item = items[i]
            smallest_idx = i

    return smallest_idx

def selection_sort(items):
    sorted_items = []

    while len(items) > 0:
        smallest_item = items.pop(find_smallest(items))
        sorted_items.append(smallest_item)

    return sorted_items


if __name__ == '__main__':
    items = [5, 3, 6, 2, 10]
    print(selection_sort(items))
