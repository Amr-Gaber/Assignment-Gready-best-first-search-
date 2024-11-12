import heapq


class Node:
    def __init__(self, name, heuristic, parent=None):
        self.name = name  # Name of the node
        self.heuristic = heuristic  # Estimated cost to the goal (heuristic value)
        self.parent = parent  # Parent node
        self.cost = 0  # Cost to reach the node (Not used in GBFS)

    def __lt__(self, other):
        return self.heuristic < other.heuristic


class GreedyBestFirstSearch:
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.graph = graph

    def search(self):
        # Priority queue (min-heap) to store nodes based on heuristic
        open_list = []

        # Set to store explored nodes
        explored = set()

        # Create start node
        start_node = Node(self.start, self.graph[self.start]['heuristic'])

        # Push the start node to the priority queue
        heapq.heappush(open_list, start_node)

        while open_list:
            # Pop the node with the lowest heuristic value
            current_node = heapq.heappop(open_list)

            # If the goal is reached, reconstruct the path
            if current_node.name == self.goal:
                path = self.reconstruct_path(current_node)
                return path

            # Add the current node to the explored set
            explored.add(current_node.name)

            # Explore neighbors
            for neighbor, neighbor_heuristic in self.graph[current_node.name]['neighbors']:
                if neighbor not in explored:
                    # Create a new node for each neighbor and push to open list
                    neighbor_node = Node(neighbor, neighbor_heuristic, current_node)
                    heapq.heappush(open_list, neighbor_node)

        return None  # No path found

    def reconstruct_path(self, node):
        path = []
        while node:
            path.append(node.name)
            node = node.parent
        path.reverse()
        return path


# Define the graph
graph = {
    'A': {'heuristic': 10, 'neighbors': [('B', 8), ('C', 7)]},
    'B': {'heuristic': 6, 'neighbors': [('A', 10), ('D', 3)]},
    'C': {'heuristic': 5, 'neighbors': [('A', 7), ('D', 2)]},
    'D': {'heuristic': 0, 'neighbors': [('B', 6), ('C', 5)]}
}

# Define the start and goal nodes
start_node = 'A'
goal_node = 'D'

# Create a GreedyBestFirstSearch object
gbfs = GreedyBestFirstSearch(start=start_node, goal=goal_node, graph=graph)

# Run the search
path = gbfs.search()

# Output the result
if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
