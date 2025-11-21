from queue import PriorityQueue
graph1 = {
    'a': [('b', 9), ('c', 4), ('d', 21)],
    'b': [('a', 9), ('c', 14), ('e', 11)],
    'c': [('a', 4), ('b', 14), ('e', 17), ('f', 18)],
    'd': [('a', 21), ('c', 7)],
    'e': [('b', 11), ('c', 17), ('z', 5)],
    'f': [('c', 18), ('z', 9)],
    'z': []
}
heuristic1 = {
    'a': 21, 'b': 14, 'c': 6,
    'd': 18, 'e': 5, 'f': 9, 'z': 0
}
def best_first_search(graph, heuristics, start, goal):
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    visited = set()
    parent = {start: None}
    while not pq.empty():
        h, node = pq.get()
        if node == goal:
            break
 visited.add(node)
        for neigh, cost in graph[node]:
            if neigh not in visited:
                pq.put((heuristics[neigh], neigh))
                parent[neigh] = node
    path = []
    n = goal
    while n is not None:
        path.append(n)
        n = parent[n]
    return path[::-1]
print("Best First Search (Graph-1):", 
      best_first_search(graph1, heuristic1, 'a', 'z'))