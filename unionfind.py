# written by Kyle Hennig (hennig1@ualberta.ca)
# August 2016
# part of the High School Intership Program (HIP)


"""
Every node should start on a different tree. When a node changes color, unite it
with all adjacent nodes of the same color. Nodes on the same tree are connected.
A player has won if nodes on opposite sides of the board are on the same tree.
"""

# Path compression.
# Make every node visited point to the same root.
def root(i, trees):
    while i != trees[i]:
        trees[i] = trees[trees[i]]
        i = trees[i]
    return i

# True if both elements are part of the same path.
def find(a, b, trees):
    return root(a, trees) == root(b, trees)

# Combines two paths together.
def unite(a, b, trees, sizes):
    i = root(a, trees)
    j = root(b, trees)
    # Avoids uniting elements in the same path.
    if i == j:
        return
    # Weighted to append the smaller path to the larger path.
    if sizes[i] < sizes[j]:
        trees[i] = j
        sizes[j] += sizes[i]
    else:
        trees[j] = i
        sizes[i] += sizes[j]
