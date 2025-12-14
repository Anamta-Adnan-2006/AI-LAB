def evaluate(board):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],   
        [0,3,6],[1,4,7],[2,5,8],   
        [0,4,8],[2,4,6]           
    ]
  for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]]:
            if board[state[0]] == 'X':
                return 1
            elif board[state[0]] == 'O':
                return -1
    return 0
def minimax(board, is_max):
    score = evaluate(board)
    if score != 0:
        return score
    if '_' not in board:
        return 0  
    if is_max:
        best = -1000
        for i in range(9):
            if board[i] == '_':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = '_'
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == '_':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = '_'
        return best
board = [
    'O','X','O',
    'O','X','X',
    'X','O','X'
]
result = minimax(board, True)
print("Game Result:", result)
