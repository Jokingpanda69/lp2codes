def bfs(graph, start_vertex):
    visited = [False] * len(graph)
    queue = [start_vertex]
    visited[start_vertex] = True

    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex, end=" ")

        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def dfs(graph, start_vertex):
    visited = [False] * len(graph)
    stack = [start_vertex]
    visited[start_vertex] = True

    while stack:
        current_vertex = stack.pop()
        print(current_vertex, end=" ")

        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True

def create_graph(vertices, edges):
    graph = [[] for _ in range(vertices)]
    for edge in edges:
        u, v = map(int, edge.split())
        graph[u].append(v)
        graph[v].append(u)  # remove this line if the graph is directed
    return graph

def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    graph = [[] for _ in range(vertices)]
    for i in range(edges):
        u, v = map(int, input(f"Enter edge {i+1} (u v): ").split())
        graph[u].append(v)
        graph[v].append(u)  # remove this line if the graph is directed

    while True:
        print("\n1. BFS")
        print("2. DFS")
        print("3. Exit")
        print("Enter your choice:")
        choice = int(input())

        if choice == 1:
            print("Enter the starting vertex:")
            start_vertex = int(input())
            bfs(graph, start_vertex)
        elif choice == 2:
            print("Enter the starting vertex:")
            start_vertex = int(input())
            dfs(graph, start_vertex)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()