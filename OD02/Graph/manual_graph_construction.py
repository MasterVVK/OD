from graph import Graph

# Создаем граф вручную
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

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
