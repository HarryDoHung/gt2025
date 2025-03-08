def create_adjacency_matrix(nodes, links):
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]
    index_map = {node: i for i, node in enumerate(nodes)}

    for start, end in links:
        matrix[index_map[start]][index_map[end]] = 1
    
    return matrix

def construct_tree(links):
    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
    
    node_map = {}
    
    for start, end in links:
        if start not in node_map:
            node_map[start] = TreeNode(start)
        if end not in node_map:
            node_map[end] = TreeNode(end)
        
        if node_map[start].left is None:
            node_map[start].left = node_map[end]
        else:
            node_map[start].right = node_map[end]
    
    return node_map

def inorder(node):
    if node is None:
        return []
    
    return inorder(node.left) + [node.key] + inorder(node.right)

def main():
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    links = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
    
    adjacency_matrix = create_adjacency_matrix(nodes, links)
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)
    
    tree_nodes = construct_tree(links)
    
    while True:
        try:
            start = int(input("Enter the starting node for Inorder traversal: "))
            if start not in tree_nodes:
                print("Invalid node")
                continue
            
            root = tree_nodes[start]
            result = inorder(root)
            print(f"\nInorder Traversal from node {start}:")
            print(" ".join(map(str, result)))
            break
        except ValueError:
            print("Enter a valid number.")

if __name__ == '__main__':
    main()
