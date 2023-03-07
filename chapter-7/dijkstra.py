graph = {
    "start": {
        "a": 5,
        "b": 2
    },
    "a": {
        "c": 4,
        "d": 2
    },
    "b": {
        "a": 8,
        "d": 7,
    },
    "c": {
        "d": 6,
        "fin": 3
    },
    "d": {
        "fin": 1
    },
    "fin": {
    }
}

infinity = float("inf")
costs = {
    "a": graph["start"]["a"],
    "b": graph["start"]["b"],
    "c": infinity,
    "d": infinity,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "c": None,
    "d": None,
    "fin": None
}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def calculate_costs(graph, costs, parents, processed):
    while len(processed) != len(costs):
        closest_node = find_lowest_cost_node(costs)
        distance = costs[closest_node]
        for neighbor in graph[closest_node]:
            new_neighbor_cost = distance + graph[closest_node][neighbor]
            if new_neighbor_cost < costs[neighbor]:
                costs[neighbor] = new_neighbor_cost
                parents[neighbor] = closest_node
        processed.append(closest_node)

def calculate_path(costs):
    path = ["fin"]
    parent = parents["fin"]
    while parent != "start":
        path.append(parent)
        parent = parents[parent]
    path.append("start")
    path.reverse()
    return path

calculate_costs(graph, costs, parents, processed)
print("Cost from the start to each node:", costs)
print("Path:", calculate_path(costs))


graph = {
    "start": {
        "a": 10
    },
    "a": {
        "b": 20
    },
    "b": {
        "c": 1,
        "fin": 30
    },
    "c": {
        "a": 1
    },
    "fin": {
    }
}

costs = {
    "a": graph["start"]["a"],
    "b": infinity,
    "c": infinity,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": None,
    "c": None,
    "fin": None
}

processed = []

calculate_costs(graph, costs, parents, processed)
print("Cost from the start to each node:", costs)
print("Path:", calculate_path(costs))
