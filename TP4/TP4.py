import heapq
from collections import defaultdict

vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = {
    (1, 2): 4, (1, 5): 1, (1, 7): 2,
    (2, 3): 7, (2, 6): 5,
    (3, 4): 1, (3, 6): 8,
    (4, 6): 6, (4, 7): 4, (4, 8): 3,
    (5, 6): 9, (5, 7): 10,
    (6, 9): 2,
    (7, 7): 2, (7, 9): 8,
    (8, 9): 1
}

adj_list = defaultdict(list)
for (u, v), weight in edges.items():
    adj_list[u].append((v, weight))
    adj_list[v].append((u, weight))

def prim(root):
    mst = []
    visited = set()
    min_heap = [(0, root, -1)]
    total_weight = 0

    while min_heap:
        weight, current, prev = heapq.heappop(min_heap)
        if current in visited:
            continue

        visited.add(current)
        if prev != -1:
            mst.append((prev, current, weight))
            total_weight += weight

        for neighbor, edge_weight in adj_list[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst, total_weight

def kruskal():
    mst = []
    total_weight = 0
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    sorted_edges = sorted(edges.items(), key=lambda x: x[1])

    for (u, v), weight in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

if __name__ == "__main__":
    root = int(input(f"Enter the root node for Prim's algorithm (choose from {vertices}): "))
    if root not in vertices:
        print("Invalid root node.")
    else:
        print("\n--- Prim's Algorithm ---")
        prim_mst, prim_weight = prim(root)
        print("Edges in MST:", prim_mst)
        print("Total weight:", prim_weight)
        
    print("\n--- Kruskal's Algorithm ---")
    kruskal_mst, kruskal_weight = kruskal()
    print("Edges in MST:", kruskal_mst)
    print("Total weight:", kruskal_weight)
