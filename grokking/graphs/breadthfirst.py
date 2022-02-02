from collections import deque
from itertools import product

def breadfirst_search(target_node, start, graph):
    search_deque = deque([start])
    searched_already = []
    while len(search_deque) > 0:
        curr_node = search_deque.popleft()
        if not curr_node in searched_already:
            searched_already.append(curr_node)
            if curr_node == target_node:
                    return True
            else:
                search_deque += graph[curr_node]
    return False


if __name__ == '__main__':
    graph = {
        "you": ["bob", "claire", "alice"],
        "bob": ["anuj", "peggy"],
        "claire": ["thom", "jonny"],
        "alice": ["peggy"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }
    starts = ["you", "bob", "anuj"]
    targets = ["thom", "alice", "anuj"]

    for start, target in list(product(starts, targets)):
        print(f'We can get from "{start}" to "{target}": {breadfirst_search(target, start, graph)}')
