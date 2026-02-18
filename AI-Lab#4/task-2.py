# -------------------------------
# Uniform Cost Search as Utility-Based Agent
# -------------------------------

import heapq

class UtilityBasedAgentUCS:
    def __init__(self, graph, goal):
        self.graph = graph
        self.goal = goal

    def ucs(self, start):
        # Priority queue (min-heap)
        queue = []
        heapq.heappush(queue, (0, start))  # (cost, node)

        visited = set()

        while queue:
            cost, node = heapq.heappop(queue)

            if node in visited:
                continue

            print("Expanding:", node, "with cost:", cost)
            visited.add(node)

            # If goal found
            if node == self.goal:
                print("Goal reached with minimum cost:", cost)
                return cost

            # Push neighbors with updated cost
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor))

        return None

    def run(self, start):
        print("\nStarting Uniform Cost Search")
        self.ucs(start)


# Example Weighted Graph
graph_ucs = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

agent_ucs = UtilityBasedAgentUCS(graph_ucs, goal='E')
agent_ucs.run('A')
# -------------------------------
# Uniform Cost Search as Utility-Based Agent
# -------------------------------

import heapq

class UtilityBasedAgentUCS:
    def __init__(self, graph, goal):
        self.graph = graph
        self.goal = goal

    def ucs(self, start):
        # Priority queue (min-heap)
        queue = []
        heapq.heappush(queue, (0, start))  # (cost, node)

        visited = set()

        while queue:
            cost, node = heapq.heappop(queue)

            if node in visited:
                continue

            print("Expanding:", node, "with cost:", cost)
            visited.add(node)

            # If goal found
            if node == self.goal:
                print("Goal reached with minimum cost:", cost)
                return cost

            # Push neighbors with updated cost
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor))

        return None

    def run(self, start):
        print("\nStarting Uniform Cost Search")
        self.ucs(start)


# Example Weighted Graph
graph_ucs = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

agent_ucs = UtilityBasedAgentUCS(graph_ucs, goal='E')
agent_ucs.run('A')
