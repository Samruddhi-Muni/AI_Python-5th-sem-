#PART-B
#  Implement AO* Search algorithm. 

# Function to calculate cost of AND / OR paths
def Cost(H, condition, weight=1):
    cost = {}

    # AND condition
    if 'AND' in condition:
        AND_nodes = condition['AND']
        path = ' AND '.join(AND_nodes)
        cost[path] = sum(H[node] + weight for node in AND_nodes)

    # OR condition
    if 'OR' in condition:
        OR_nodes = condition['OR']
        path = ' OR '.join(OR_nodes)
        cost[path] = min(H[node] + weight for node in OR_nodes)

    return cost


# Function to update heuristic costs
def update_cost(H, Conditions, weight=1):
    updated_cost = {}

    # Process nodes in reverse order (bottom-up)
    for node in reversed(list(Conditions.keys())):
        condition = Conditions[node]
        cost = Cost(H, condition, weight)
        print(node, ":", condition, ">>>", cost)

        # Update heuristic with minimum cost
        H[node] = min(cost.values())
        updated_cost[node] = cost

    return updated_cost


# Function to find shortest AO* path
def shortest_path(start, updated_cost):
    if start not in updated_cost:
        return start

    costs = updated_cost[start]
    min_cost = min(costs.values())

    for path, value in costs.items():
        if value == min_cost:
            nodes = path.split()

            # OR path (single node)
            if len(nodes) == 1:
                return start + " <-- " + shortest_path(nodes[0], updated_cost)

            # AND path (multiple nodes)
            else:
                left = shortest_path(nodes[0], updated_cost)
                right = shortest_path(nodes[-1], updated_cost)
                return start + " <-- (" + nodes[0] + " AND " + nodes[-1] + ") [" + left + " + " + right + "]"


# Heuristic values
H = {
    'A': -1, 'B': 5, 'C': 2, 'D': 4,
    'E': 7, 'F': 9, 'G': 3,
    'H': 0, 'I': 0, 'J': 0
}

# Graph conditions
Conditions = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}

# Edge weight
weight = 1

print("Updated Cost:")
updated_cost = update_cost(H, Conditions, weight)

print("\n" + "*" * 70)
print("Shortest Path:")
print(shortest_path('A', updated_cost))
