import math

def alphabeta(node, depth, alpha, beta, is_max, tree):
    # Terminal node
    if isinstance(tree[node], int):
        return tree[node]

    if is_max:
        value = -math.inf
        for child in tree[node]:
            value = max(value, alphabeta(child, depth+1, alpha, beta, False, tree))
            alpha = max(alpha, value)
            if alpha >= beta:
                break   # PRUNING
        return value
    else:
        value = math.inf
        for child in tree[node]:
            value = min(value, alphabeta(child, depth+1, alpha, beta, True, tree))
            beta = min(beta, value)
            if beta <= alpha:
                break   # PRUNING
        return value


# Game tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': 4,
    'I': 2,
    'J': -3,
    'K': -6,
    'L': 7,
    'M': 0,
    'N': 5,
    'O': 8
}

result = alphabeta('A', 0, -math.inf, math.inf, True, tree)
print("Optimal value at root (A):", result)
