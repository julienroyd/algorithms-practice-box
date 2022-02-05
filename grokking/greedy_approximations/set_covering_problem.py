def greedy_set_covering(set_to_cover, blanket_coverage):
    chosen_blankets = set()
    uncovered = set_to_cover - set().union(*[blanket_coverage[b] for b in chosen_blankets])

    while uncovered:
        available_blankets = set(stations.keys()) - chosen_blankets
        best_blanket = None
        best_coverage = 0
        for b in available_blankets:
            n_newly_covered = len(uncovered & blanket_coverage[b])
            if n_newly_covered > best_coverage:
                best_blanket = b
                best_coverage = n_newly_covered
        chosen_blankets.add(best_blanket)
        uncovered -= blanket_coverage[best_blanket]

    return chosen_blankets


if __name__ == '__main__':
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }
    chosen_stations = greedy_set_covering(set_to_cover=states_needed, blanket_coverage=stations)
    covered_states  = set().union(*[stations[s] for s in chosen_stations])
    print(f"The set of stations {chosen_stations} covers {len(covered_states)} states: {covered_states}")
