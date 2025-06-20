import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain  # Louvain method = modularity optimization

# 1. Create a weighted social graph (sample echo chamber data)
# You can modify this part to load real-world data, for example from a CSV, JSON, or network dataset (e.g. SNAP, Twitter API, etc.)
G = nx.Graph()

### Uncommand this to using strong community data, means weak strong chamber
# edges = [
#     # 🔵 Community A (Echo Chamber A)
#     ('Luna', 'Rex', 6), ('Luna', 'Zane', 5), ('Luna', 'Mira', 4),
#     ('Rex', 'Zane', 5), ('Rex', 'Mira', 6), ('Zane', 'Mira', 5),
#     ('Zane', 'Kira', 4), ('Mira', 'Kira', 5),

#     # 🔴 Community B (Echo Chamber B)
#     ('Nova', 'Axel', 6), ('Nova', 'Sage', 4), ('Nova', 'Lex', 5),
#     ('Axel', 'Sage', 4), ('Axel', 'Lex', 5), ('Sage', 'Lex', 6),
#     ('Lex', 'Tara', 3), ('Sage', 'Tara', 4),

#     # 🟢 Community C (Echo Chamber C)
#     ('Yuna', 'Vega', 6), ('Yuna', 'Kai', 5), ('Yuna', 'Niko', 5),
#     ('Vega', 'Kai', 4), ('Kai', 'Niko', 5), ('Niko', 'Orin', 4),

#     # 🌐 Cross-community interactions (weaker connections)
#     ('Rex', 'Axel', 1), ('Zane', 'Yuna', 1), ('Nova', 'Orin', 2),
#     ('Luna', 'Kai', 1), ('Tara', 'Kira', 2),
# ]
### uncommand until this

### Uncommand this to using weak community interaction, means weak echo chamber
edges = [
    ('Luna', 'Nova', 6), ('Luna', 'Axel', 5), ('Luna', 'Yuna', 4),
    ('Rex', 'Kai', 6), ('Rex', 'Lex', 5), ('Rex', 'Mira', 4),
    ('Zane', 'Sage', 5), ('Zane', 'Tara', 6), ('Zane', 'Kira', 4),
    ('Nova', 'Zane', 5), ('Nova', 'Kira', 4), ('Nova', 'Orin', 6),
    ('Kai', 'Vega', 5), ('Kai', 'Mira', 4), ('Kai', 'Tara', 5),
    ('Lex', 'Yuna', 6), ('Lex', 'Niko', 5), ('Lex', 'Axel', 4),
    ('Sage', 'Mira', 5), ('Sage', 'Yuna', 6), ('Sage', 'Rex', 5),
    ('Tara', 'Orin', 4), ('Tara', 'Kira', 5), ('Tara', 'Luna', 4),
    ('Kira', 'Vega', 5), ('Kira', 'Niko', 4), ('Kira', 'Axel', 5),
    ('Niko', 'Zane', 5), ('Niko', 'Yuna', 6), ('Niko', 'Vega', 5),
    ('Mira', 'Orin', 4), ('Mira', 'Lex', 5), ('Mira', 'Vega', 6)
]
### uncommand until this

G.add_weighted_edges_from(edges)

# 2. Apply modularity-based community detection
partition = community_louvain.best_partition(G, weight='weight')
modularity = community_louvain.modularity(partition, G, weight='weight')
print("Modularity score:", modularity)

# 3. Visualize detected communities
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
colors = [partition[n] for n in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_color=colors, cmap=plt.cm.Set2, node_size=800)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, width=1.5)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}
)

plt.title("Detecting Echo Chamber Communities via Modularity Optimization")
plt.axis('off')
plt.tight_layout()
### to save the graph to a photo file with the given name
### UNCOMMAND ONE OF THE TWO LINES BELOW
# plt.savefig("strong_echo_chambers_communities.png", dpi=300, bbox_inches='tight')
# plt.savefig("weak_echo_chambers_communities.png", dpi=300, bbox_inches='tight')
plt.show()