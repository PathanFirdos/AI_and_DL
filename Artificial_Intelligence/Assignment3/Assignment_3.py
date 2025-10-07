import networkx as nx
import matplotlib.pyplot as plt

# --- Build the family tree ---
G = nx.DiGraph()

# Add family members
G.add_nodes_from([
    "john", "mary", "paul", "linda", "kevin", "emma", "alice", "bob"
])

# Add parent-child relationships
G.add_edges_from([
    ("john", "paul"),
    ("mary", "paul"),
    ("john", "linda"),
    ("mary", "linda"),
    ("paul", "kevin"),
    ("linda", "emma"),
    ("paul", "alice"),
    ("linda", "bob")
])

# --- Relationship check functions ---
def is_parent(parent, child):
    return G.has_edge(parent, child)

def is_grandparent(grandparent, grandchild):
    for child in G.successors(grandparent):
        if G.has_edge(child, grandchild):
            return True
    return False

def are_siblings(a, b):
    parents_a = set(G.predecessors(a))
    parents_b = set(G.predecessors(b))
    return len(parents_a & parents_b) > 0

# --- Test relationships ---
print("Is John father of Mary?", is_parent("john", "mary"))
print("Is John grandparent of Alice?", is_grandparent("john", "alice"))
print("Are Alice and Bob siblings?", are_siblings("alice", "bob"))
print("Is Mary mother of Alice?", is_parent("mary", "alice"))

# --- DAG-friendly top-down layout ---
# Define layers manually
layer_mapping = {
    0: ["john", "mary"],              # grandparents
    1: ["paul", "linda"],             # parents
    2: ["kevin", "emma", "alice", "bob"]  # children
}

# Reverse mapping: node -> layer
subset_dict = {}
for layer, nodes in layer_mapping.items():
    for node in nodes:
        subset_dict[node] = layer

# Assign node attribute for multipartite_layout
for node, layer in subset_dict.items():
    G.nodes[node]['subset'] = layer

# Compute positions
pos = nx.multipartite_layout(G, subset_key='subset')

# Flip y-axis so root (grandparents) is on top
for node in pos:
    pos[node] = (pos[node][0], -pos[node][1])

# --- Draw the family tree ---
plt.figure(figsize=(10, 6))
nx.draw(G, pos=pos, with_labels=True, arrows=True,
        node_size=2500, node_color="lightgreen", font_size=10)
plt.title("Family Tree (DAG-compatible)")
plt.show()



