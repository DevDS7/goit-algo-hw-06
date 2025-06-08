import networkx as nx
from collections import deque

#Створення графа
G = nx.Graph()

stations = [
    "Вокзальна", "Майдан Незалежності", "Площа Українських Героїв",
    "Золоті Ворота", "Героїв Дніпра", "Хрещатик",
    "Житомирська", "Лук'янівська", "Палац Спорту"
]

G.add_nodes_from(stations)

edges = [
    ("Житомирська", "Вокзальна"),
    ("Вокзальна", "Хрещатик"),
    ("Хрещатик", "Майдан Незалежності"),
    ("Майдан Незалежності", "Площа Українських Героїв"),
    ("Майдан Незалежності", "Героїв Дніпра"),
    ("Площа Українських Героїв", "Палац Спорту"),
    ("Палац Спорту", "Золоті Ворота"),
    ("Золоті Ворота", "Лук'янівська")
]

G.add_edges_from(edges)

#Перетворення на словник
graph = nx.to_dict_of_lists(G)

#BFS (рекурсивно)
def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

#DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("BFS (від Житомирська):")
bfs_recursive(graph, deque(["Житомирська"]))
print("\nDFS (від Житомирська):")
dfs(graph, "Житомирська")