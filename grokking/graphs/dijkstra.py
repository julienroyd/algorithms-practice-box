def dijkstra_search(graph, start, target):
    costs = {k: float('inf') for k in graph.keys()}
    parents = {k: None for k in graph.keys()}

    cheapest_node = start
    costs[start] = 0.
    to_process = list(graph.keys())
    to_process.remove(start)

    while len(to_process) > 0:
        # Update children's cost and parent
        children_edge_costs = graph[cheapest_node]
        for child in children_edge_costs.keys():
            candidate_cost = children_edge_costs[child] + costs[cheapest_node]
            if candidate_cost < costs[child]:
                costs[child] = candidate_cost
                parents[child] = cheapest_node

        # Go to next cheapest node
        cheapest_node = [k for k, v in sorted(costs.items(), key=lambda item: item[1]) if k in to_process][0]
        to_process.remove(cheapest_node)

    # Compute shortest path
    shortest_path = [target]
    next_parent = parents[target]
    while next_parent is not None:
        shortest_path.append(next_parent)
        next_parent = parents[shortest_path[-1]]

    return list(reversed(shortest_path)), costs[target]


if __name__ == '__main__':
    graph = {
        "Start": {"A": 6, "B": 2},
        "A": {"Fin": 1},
        "B": {"A": 3, "Fin": 5},
        "Fin": {}
    }
    start = "Start"
    target = "Fin"
    path, cost = dijkstra_search(graph, start, target)
    print(f"The shortest path between '{start}' and '{target}' is {path} and costs {cost}")

    start = "B"
    target = "Fin"
    path, cost = dijkstra_search(graph, start, target)
    print(f"The shortest path between '{start}' and '{target}' is {path} and costs {cost}")

    start = "Start"
    target = "A"
    path, cost = dijkstra_search(graph, start, target)
    print(f"The shortest path between '{start}' and '{target}' is {path} and costs {cost}")
