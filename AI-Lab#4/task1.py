# -------------------------------
# Depth Limited Search as Goal-Based Agent
# -------------------------------

class GoalBasedAgentDLS:
    def __init__(self, graph, goal, depth_limit):
        self.graph = graph              # Graph as adjacency list
        self.goal = goal                # Goal node
        self.depth_limit = depth_limit  # Maximum depth allowed

    def dls(self, current_node, depth):
        print("Visiting:", current_node, "Depth:", depth)

        # Check if goal is reached
        if current_node == self.goal:
            return True

        # If depth limit reached, stop exploring further
        if depth == self.depth_limit:
            return False

        # Explore neighbors
        for neighbor in self.graph.get(current_node, []):
            found = self.dls(neighbor, depth + 1)
            if found:
                return True

        return False

    def run(self, start_node):
        print("\nStarting Depth-Limited Search")
        result = self.dls(start_node, 0)

        if result:
            print("Goal found within depth limit!")
        else:
            print("Goal not found within depth limit.")


# Example Graph
graph_dls = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

agent_dls = GoalBasedAgentDLS(graph_dls, goal='E', depth_limit=2)
agent_dls.run('A')
