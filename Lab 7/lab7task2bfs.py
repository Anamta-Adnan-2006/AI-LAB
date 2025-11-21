graph = {
    'S': {'A': 4, 'B': 10, 'C': 11},
    'A': {'D': 5, 'B': 8},
    'B': {'D': 15},
    'C': {'B': 8, 'D': 20, 'E': 2},
    'D': {'H': 16, 'I': 20, 'F': 1},
    'E': {'G': 19},
    'F': {'G': 13},
    'H': {'I': 1, 'J': 2},
    'I': {'J': 5, 'K': 13, 'G': 5},
    'J': {'K': 7},
    'K': {'G': 16},
    'G': {}
}
h = {
    'S': 7, 'A': 8, 'B': 6, 'C': 5,
    'D': 5, 'E': 3, 'F': 3, 'G': 0,
    'H': 7, 'I': 4, 'J': 5, 'K': 3
}
def best_first_search(start, goal):
    frontier = [(h[start], start, [start])]     
    visited = set()
while frontier:
        frontier.sort()                         
        _, node, path = frontier.pop(0)
        if node == goal:
            return path
        visited.add(node)
  for neigh in graph[node]:
            if neigh not in visited:
                frontier.append((h[neigh], neigh, path + [neigh]))
return None
path = best_first_search('S', 'G')
print("Best First Search Path:", path)
