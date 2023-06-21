class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Verteks yang sama %d dan %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("Tidak terdapat edge antara %d dan %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

g.print_matrix()


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 0)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(3, 0)
graph.print_graph()


def dfs(graphx, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graphx[start] - visited:
        dfs(graphx, next, visited)
    return visited


def bfs(graphx, root):
    visited, queue = set(), graphx.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graphx[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

