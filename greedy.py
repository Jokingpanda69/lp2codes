import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        visited = [False] * self.V
        mst_weight = 0
        pq = [(0, 0)]  # Priority queue to store (weight, vertex) pairs
        while pq:
            weight, u = heapq.heappop(pq)
            if not visited[u]:
                visited[u] = True
                mst_weight += weight
                for v, w in self.graph[u]:
                    if not visited[v]:
                        heapq.heappush(pq, (w, v))
        return mst_weight

    def kruskal_mst(self):
        parent = list(range(self.V))
        find = lambda x: x if parent[x] == x else find(parent[x])
        mst_weight = 0
        edges = []
        for u in range(self.V):
            for v, w in self.graph[u]:
                edges.append((u, v, w))
        edges.sort(key=lambda x: x[2])
        for edge in edges:
            u, v, weight = edge
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                mst_weight += weight
        return mst_weight

    def dijkstra_shortest_path(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            distance, u = heapq.heappop(pq)
            if distance > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

print("Prim's MST Weight:", g.prim_mst())
print("Kruskal's MST Weight:", g.kruskal_mst())
print("Shortest paths from vertex 0 using Dijkstra:", g.dijkstra_shortest_path(0))
