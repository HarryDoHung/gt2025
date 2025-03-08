from collections import defaultdict, deque

def convert_to_adj_matrix(edge_list, total_nodes):
    matrix = [[0] * total_nodes for _ in range(total_nodes)]
    for start, end in edge_list:
        matrix[start - 1][end - 1] = 1
    return matrix

def display_matrix(matrix):
    print("Adjacency Matrix:")
    for line in matrix:
        print(" ".join(map(str, line)))

def matrix_to_adj_list(matrix):
    adjacency_list = defaultdict(list)
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == 1:
                adjacency_list[row_index + 1].append(col_index + 1)
    return adjacency_list

def count_weak_components(matrix):
    adj_list = matrix_to_adj_list(matrix)
    undirected_graph = defaultdict(list)
    
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            undirected_graph[node].append(neighbor)
            undirected_graph[neighbor].append(node)
    
    visited = set()
    component_count = 0
    
    def bfs(start):
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for adjacent in undirected_graph[current]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)
    
    for node in range(1, len(matrix) + 1):
        if node not in visited:
            component_count += 1
            visited.add(node)
            bfs(node)
    
    return component_count

def count_strong_components(matrix):
    adj_list = matrix_to_adj_list(matrix)
    visited = set()
    order = []
    
    def forward_dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                forward_dfs(neighbor)
        order.append(node)
    
    for node in range(1, len(matrix) + 1):
        if node not in visited:
            forward_dfs(node)
    
    reversed_adj_list = defaultdict(list)
    for start, destinations in adj_list.items():
        for dest in destinations:
            reversed_adj_list[dest].append(start)
    
    visited.clear()
    strong_count = 0
    
    def reverse_dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(reversed_adj_list[current])
    
    while order:
        node = order.pop()
        if node not in visited:
            strong_count += 1
            reverse_dfs(node)
    
    return strong_count

if __name__ == "__main__":
    edge_data = [
        (1, 2), (1, 4), (2, 3), (2, 6),
        (6, 3), (6, 4), (5, 4), (7, 6),
        (7, 3), (7, 5), (7, 8), (8, 9), (5, 9)
    ]
    total_nodes = 9

    adjacency_matrix = convert_to_adj_matrix(edge_data, total_nodes)

    display_matrix(adjacency_matrix)

    weak_components = count_weak_components(adjacency_matrix)
    strong_components = count_strong_components(adjacency_matrix)

    print(f"\nWeak components: {weak_components}")
    print(f"Strong components: {strong_components}")
