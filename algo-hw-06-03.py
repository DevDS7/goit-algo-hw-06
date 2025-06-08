import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    "Вокзальна", "Майдан Незалежності", "Площа Українських Героїв",
    "Золоті Ворота", "Героїв Дніпра", "Хрещатик",
    "Житомирська", "Лук'янівська", "Палац Спорту"
]

G.add_nodes_from(stations)

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

G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

#Обрахунок найкоротших шляхів
for source in G.nodes:
    lengths, paths = nx.single_source_dijkstra(G, source)
    print(f"\n🔹 Найкоротші шляхи від '{source}':")
    for target in G.nodes:
        if source != target:
            print(f"  до '{target}': відстань = {lengths[target]}, шлях = {' → '.join(paths[target])}")

length, path = nx.single_source_dijkstra(G, source="Житомирська", target="Лук'янівська")
print(f"\n🚆 Найкоротший шлях з Житомирської до Лук'янівської: {path} (відстань: {length})")