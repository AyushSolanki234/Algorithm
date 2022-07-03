from collections import defaultdict


class Graph:
    def __init__(self, vert):
        self.graph = defaultdict(list)
        self.V = vert

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def TopologicalSort(self, v, visit, stack):

        visit[v] = True

        for i in self.graph[v]:
            if visit[i] == False:
                self.TopologicalSort(i, visit, stack)

        stack.append(v)

    def topologicalSort(self):
        visit = [False] * self.V
        stack = []

        for i in range(self.V):
            if visit[i] == False:
                self.TopologicalSort(i, visit, stack)
        print(stack[::-1])


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Topological Sort is ")

g.topologicalSort()
