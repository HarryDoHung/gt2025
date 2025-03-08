import heapq

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
node_index = {node: idx for idx, node in enumerate(nodes)}
node_count = len(nodes)

adj_matrix = [[float('inf')] * node_count for _ in range(node_count)]

edges = [
    ('A', 'C', 1), ('A', 'B', 4),
    ('B', 'F', 3),
    ('C', 'D', 8), ('C', 'F', 7),
    ('D', 'H', 5),
    ('F', 'H', 1), ('F', 'E', 1),
    ('E', 'H', 2),
    ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
    ('G', 'M', 4),
    ('M', 'L', 1),
    ('L', 'G', 4), ('L', 'E', 2)
]

for u, v, weight in edges:
    u_idx, v_idx = node_index[u], node_index[v]
    adj_matrix[u_idx][v_idx] = weight
    adj_matrix[v_idx][u_idx] = weight  

def display_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print("  ".join("∞" if val == float('inf') else str(val) for val in row))

display_matrix(adj_matrix)

index_to_node = {idx: node for node, idx in node_index.items()}

def dijkstra(matrix, start, end):
    start_idx, end_idx = node_index[start], node_index[end]
    distances = [float('inf')] * node_count
    distances[start_idx] = 0
    prev_nodes = [None] * node_count
    pq = [(0, start_idx)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor_idx, weight in enumerate(matrix[curr_node]):
            if weight != float('inf'):
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor_idx]:
                    distances[neighbor_idx] = new_dist
                    prev_nodes[neighbor_idx] = curr_node
                    heapq.heappush(pq, (new_dist, neighbor_idx))

    path = []
    curr = end_idx
    while curr is not None:
        path.append(index_to_node[curr])
        curr = prev_nodes[curr]
    path.reverse()

    return path, distances[end_idx]

start_node = input("Enter source node (A-M): ").strip().upper()
end_node = input("Enter target node (A-M): ").strip().upper()

if start_node in node_index and end_node in node_index:
    shortest_path, total_weight = dijkstra(adj_matrix, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
    print(f"Total weight of the path: {total_weight}")
else:
    print("Invalid input. Please enter a valid node (A-M).")
