import networkx as nx
import matplotlib.pyplot as plt

# 1. Create a weighted social graph (sample echo chamber data)
G = nx.Graph()

### Uncommand this to using strong community data, means weak strong chamber
edges = [
    # 🔵 Community A (Echo Chamber A)
    ('Luna', 'Rex', 6), ('Luna', 'Zane', 5), ('Luna', 'Mira', 4),
    ('Rex', 'Zane', 5), ('Rex', 'Mira', 6), ('Zane', 'Mira', 5),
    ('Zane', 'Kira', 4), ('Mira', 'Kira', 5),

    # 🔴 Community B (Echo Chamber B)
    ('Nova', 'Axel', 6), ('Nova', 'Sage', 4), ('Nova', 'Lex', 5),
    ('Axel', 'Sage', 4), ('Axel', 'Lex', 5), ('Sage', 'Lex', 6),
    ('Lex', 'Tara', 3), ('Sage', 'Tara', 4),

    # 🟢 Community C (Echo Chamber C)
    ('Yuna', 'Vega', 6), ('Yuna', 'Kai', 5), ('Yuna', 'Niko', 5),
    ('Vega', 'Kai', 4), ('Kai', 'Niko', 5), ('Niko', 'Orin', 4),

    # 🌐 Cross-community interactions (weaker connections)
    ('Rex', 'Axel', 1), ('Zane', 'Yuna', 1), ('Nova', 'Orin', 2),
    ('Luna', 'Kai', 1), ('Tara', 'Kira', 2),
]
### uncommand until this

### Uncommand this to using weak community interaction, means weak echo chamber
# edges = [
#     ('Luna', 'Nova', 6), ('Luna', 'Axel', 5), ('Luna', 'Yuna', 4),
#     ('Rex', 'Kai', 6), ('Rex', 'Lex', 5), ('Rex', 'Mira', 4),
#     ('Zane', 'Sage', 5), ('Zane', 'Tara', 6), ('Zane', 'Kira', 4),
#     ('Nova', 'Zane', 5), ('Nova', 'Kira', 4), ('Nova', 'Orin', 6),
#     ('Kai', 'Vega', 5), ('Kai', 'Mira', 4), ('Kai', 'Tara', 5),
#     ('Lex', 'Yuna', 6), ('Lex', 'Niko', 5), ('Lex', 'Axel', 4),
#     ('Sage', 'Mira', 5), ('Sage', 'Yuna', 6), ('Sage', 'Rex', 5),
#     ('Tara', 'Orin', 4), ('Tara', 'Kira', 5), ('Tara', 'Luna', 4),
#     ('Kira', 'Vega', 5), ('Kira', 'Niko', 4), ('Kira', 'Axel', 5),
#     ('Niko', 'Zane', 5), ('Niko', 'Yuna', 6), ('Niko', 'Vega', 5),
#     ('Mira', 'Orin', 4), ('Mira', 'Lex', 5), ('Mira', 'Vega', 6)
# ]
### uncommand until this

G.add_weighted_edges_from(edges)

# 2. Visualize the graph (no community detection)
plt.figure(figsize=(8, 6))
pos = nx.random_layout(G)

# Default node color (uniform)
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=800)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, width=1.5)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}
)

plt.title("Synthetic Echo Chamber Network (No Community Detection)")
plt.axis('off')
plt.tight_layout()
### to save the graph to a photo file with the given name
### UNCOMMAND ONE OF THE TWO LINES BELOW
# plt.savefig("Weak Echo Chamber Network (No Community Detection).png", dpi=300, bbox_inches='tight')
# plt.savefig("Strong Echo Chamber Network (No Community Detection).png", dpi=300, bbox_inches='tight')
plt.show()
