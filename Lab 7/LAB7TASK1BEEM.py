graph = {
    'a': {'b': 9, 'c': 4, 'd': 7},
    'b': {'a': 9, 'e': 11},
    'c': {'a': 4, 'e': 17, 'f': 12},
    'd': {'a': 7, 'f': 14},
    'e': {'b': 11, 'c': 17, 'z': 5},
    'f': {'c': 12, 'd': 14, 'z': 9},
    'z': {'e': 5, 'f': 9}
}
h = {
    'a': 21, 'b': 14, 'c': 18, 
    'd': 18, 'e': 5, 'f': 8, 
    'z': 0
}
def beam_search(start, goal, beam_width):
  frontier = [(start, [start])]       # (node, path)
    while frontier:
        successors = []
 for node, path in frontier:
            if node == goal:
                return path
            for neigh, cost in graph[node].items():
                if neigh not in path:
                    successors.append((neigh, path + [neigh]))
        if not successors:
            return None
        successors.sort(key=lambda x: h[x[0]])
        frontier = successors[:beam_width]
 return None
path = beam_search('a', 'z', beam_width=2)
print("Beam Search Path:", path)
