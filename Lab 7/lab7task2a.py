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
import heapq
def a_star(start, goal):
    pq = []                           
    heapq.heappush(pq, (h[start], 0, start, [start]))  
 visited = {}
 while pq:
        f, g, node, path = heapq.heappop(pq)
if node == goal:
            return path, g
 if node in visited and visited[node] <= g:
            continue
  visited[node] = g
 for neigh, cost in graph[node].items():
            new_g = g + cost
            new_f = new_g + h[neigh]
            heapq.heappush(pq, (new_f, new_g, neigh, path + [neigh]))
 return None, None
path, cost = a_star('S', 'G')
print("A* Path:", path)
print("Total Cost:", cost)
