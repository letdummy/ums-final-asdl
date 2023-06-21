import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class GraphVisualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

    def bfs(self, start, end):
        # Creating a visited list to keep track of visited nodes
        visited = set()
        # Creating a queue for BFS
        queue = deque()
        # Enqueue the start node and mark it as visited
        queue.append([start])
        visited.add(start)

        while queue:
            # Dequeue a path from the queue
            path = queue.popleft()
            current_node = path[-1]

            # Check if we reached the destination node
            if current_node == end:
                print("Found a path from", start, "to", end)
                return path

            # Get all the adjacent vertices of the current node
            for edge in self.visual:
                if current_node in edge:
                    neighbor = edge[0] if edge[0] != current_node else edge[1]
                    # If the neighbor has not been visited, enqueue its path and mark it as visited
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
                        visited.add(neighbor)

        print("No path found from", start, "to", end)
        return []

    def dfs(self, start, end):
        # Creating a visited list to keep track of visited nodes
        visited = set()

        def dfs_util(current_node, path):
            # Mark the current node as visited
            visited.add(current_node)

            # Check if we reached the destination node
            if current_node == end:
                print("Found a path from", start, "to", end)
                return path

            # Recur for all the adjacent vertices of the current node
            for edge in self.visual:
                if current_node in edge:
                    neighbor = edge[0] if edge[0] != current_node else edge[1]
                    # If the neighbor has not been visited, recursively call dfs_util on it
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        result = dfs_util(neighbor, new_path)
                        if result:
                            return result

            return []

        return dfs_util(start, [start])


# Driver code
G = GraphVisualization()
G.addEdge(5, 6)
G.addEdge(7, 3)
G.addEdge(1, 2)
G.addEdge(8, 2)
G.addEdge(2, 3)
G.addEdge(2, 6)
G.addEdge(3, 6)
G.addEdge(4, 3)
G.addEdge(4, 6)
G.visualize()
bfs_path = G.bfs(5, 4)
print("BFS path:", bfs_path)

dfs_path = G.dfs(5, 4)
print("DFS path:", dfs_path)
