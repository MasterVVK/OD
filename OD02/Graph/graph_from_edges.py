from graph import Graph

# Построение графа из списка ребер
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
g = Graph()
vertices = set(sum(edges, ()))
for vertex in vertices:
    g.add_vertex(vertex)
for edge in edges:
    g.add_edge(*edge)

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
