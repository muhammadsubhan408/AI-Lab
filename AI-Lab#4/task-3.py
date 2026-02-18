# -------------------------------
# Traveling Salesman Problem (Brute Force)
# -------------------------------

import itertools

def tsp_bruteforce(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))

    min_path = None
    min_cost = float('inf')

    # Fix starting city as 0
    for perm in itertools.permutations(cities[1:]):
        path = [0] + list(perm) + [0]  # return to start
        cost = 0

        # Calculate total cost
        for i in range(len(path) - 1):
            cost += distance_matrix[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost


# Example Distance Matrix
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_bruteforce(distance_matrix)

print("\nShortest TSP Path:", path)
print("Minimum Cost:", cost)
