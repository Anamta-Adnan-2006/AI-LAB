graph2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E', 'I'],
    'D': ['J'],
    'E': ['J'],
    'I': ['F', 'J'],
    'F': [],
    'J': ['K', 'L'],
    'K': [],
    'L': []
}
def dls(node, depth):
    if depth < 0:
        return []
    if depth == 0:
        return [node]
    result = [node]
    for child in graph2[node]:
        result += dls(child, depth - 1)
    return result
def iddfs(start, max_depth):
    result = []
    for depth in range(max_depth + 1):
        result.append(dls(start, depth))
    return result


# ---- PRINT IDDFS OUTPUT ----
print("IDDFS Result:", iddfs('A', 4))
