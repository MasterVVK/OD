from graph import Graph

# Построение графа из матрицы смежности
adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

g = Graph()
vertices = range(1, len(adj_matrix) + 1)
for vertex in vertices:
    g.add_vertex(vertex)

for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix)):
        if adj_matrix[i][j] == 1:
            g.add_edge(i + 1, j + 1)

# Печать графа
print("Список смежности графа:")
for vertex, edges in g.graph.items():
    print(f"Вершина {vertex}: соединена с {edges}")

# Выполнение обхода в глубину (DFS)
print("\nОбход в глубину (DFS) начиная с вершины 1:")
g.dfs(1)

# Выполнение обхода в ширину (BFS)
print("\nОбход в ширину (BFS) начиная с вершины 1:")
g.bfs(1)
