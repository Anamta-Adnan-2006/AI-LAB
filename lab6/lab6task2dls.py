graph = {
    'A': ['B', 'C', 'E'],
    'B': ['D'],
    'C': ['F', 'I', 'E'],
    'D': ['H'],
    'E': ['H', 'J'],
    'F': [],
    'H': [],
    'I': ['J', 'G'],
    'J': ['G'],
    'G': []
}
def dls(start, depth):
    if depth < 0:
        return []
    if depth == 0:
        return [start]
    order = [start]
    for n in graph2[start]:
        order += dls(n, depth - 1)
    return order
