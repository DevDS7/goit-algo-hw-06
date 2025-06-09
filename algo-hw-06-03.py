import heapq

def dijkstra_manual(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, target):
    path = []
    current_node = target
    while current_node != start:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.append(start)
    return path[::-1]

stations = [
    "Вокзальна", "Майдан Незалежності", "Площа Українських Героїв",
    "Золоті Ворота", "Героїв Дніпра", "Хрещатик",
    "Житомирська", "Лук'янівська", "Палац Спорту"
]

edges = [
    ("Житомирська", "Вокзальна", {"weight": 5}),
    ("Вокзальна", "Хрещатик", {"weight": 4}),
    ("Хрещатик", "Майдан Незалежності", {"weight": 1}),
    ("Майдан Незалежності", "Площа Українських Героїв", {"weight": 5}),
    ("Майдан Незалежності", "Героїв Дніпра", {"weight": 35}),
    ("Площа Українських Героїв", "Палац Спорту", {"weight": 1}),
    ("Палац Спорту", "Золоті Ворота", {"weight": 1}),
    ("Золоті Ворота", "Лук'янівська" , {"weight": 4})
]

graph = {station: [] for station in stations} 

for u, v, w in edges:
    graph[u].append((v, w["weight"]))
    graph[v].append((u, w["weight"]))

distances, previous = dijkstra_manual(graph, "Житомирська")
shortest_path = reconstruct_path(previous, "Житомирська", "Лук'янівська")
distances["Лук'янівська"], shortest_path

print(f"Shortest distance from Житомирська to Лук'янівська: {distances['Лук\'янівська']}")
print(f"Shortest path from Житомирська to Лук'янівська: {' -> '.join(shortest_path)}")