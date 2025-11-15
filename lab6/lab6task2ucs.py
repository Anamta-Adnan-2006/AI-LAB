import heapq
weighted_graph = {
    'A': [('B', 2), ('C', 3), ('E', 5)],
    'B': [('D', 1)],
    'C': [('F', 4), ('I', 2), ('E', 3)],
    'D': [('H', 2)],
    'E': [('H', 3), ('J', 4)],
    'F': [],
    'H': [],
    'I': [('J', 1), ('G', 6)],
    'J': [('G', 2)],
    'G': []
}
def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]  # (cost, node, path)
        while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        print(f"Visiting {node} with cost {cost}")
            if node == goal:
            print(f"\nGoal {goal} reached with total cost {cost}")
            print(f"Path: {' -> '.join(path)}")
            return
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path))
    print(f"\nGoal {goal} not reachable from {start}")
print("\nUCS from A to G:")
ucs(weighted_graph, 'A', 'G')