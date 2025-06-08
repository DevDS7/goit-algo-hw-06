import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#Додаємо вершини (станції)
stations = [
    "Вокзальна", "Майдан Незалежності", "Площа Українських Героїв",
    "Золоті Ворота", "Героїв Дніпра", "Хрещатик",
    "Житомирська", "Лук'янівська", "Палац Спорту"
]

G.add_nodes_from(stations)

#Додаємо ребра
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

#Аналіз характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

print("\nСтупінь вершин:")
for node, degree in G.degree():
    print(f"{node}: {degree}")

#Центральності
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print("\nDegree Centrality:")
for node, val in degree_centrality.items():
    print(f"{node}: {val:.3f}")

print("\nCloseness Centrality:")
for node, val in closeness_centrality.items():
    print(f"{node}: {val:.3f}")

print("\nBetweenness Centrality:")
for node, val in betweenness_centrality.items():
    print(f"{node}: {val:.3f}")

#Візуалізація
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
plt.show()