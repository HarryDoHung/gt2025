from collections import defaultdict, deque

class DirectedGraph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def insert_edge(self, from_node, to_node):
        self.adjacency_list[from_node].append(to_node)

    def has_path(self, source, destination):
        visited = set()
        queue = deque([source])

        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
            
            visited.add(node)
            
            for adjacent in self.adjacency_list[node]:
                if adjacent not in visited and adjacent not in queue:
                    queue.append(adjacent)
        
        return False

network = DirectedGraph()

connections = [
    (1, 2), (2, 5), (3, 6), (4, 6), (6, 7), (4, 7)
]

for start, end in connections:
    network.insert_edge(start, end)

begin = int(input("Start node: "))
end = int(input("End node: "))

print("Exist" if network.has_path(begin, end) else "Do not exist")
