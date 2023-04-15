import math

# Constants representing the players and the empty cell

X = 'X'
O = 'O'
EMPTY = '-'

# Function to print the game board

def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to check if a player has won

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    # Player has not won
    return False

# Function to evaluate the game board for the minimax algorithm

def evaluate_board(board):
    if check_win(board, X):
        return 1
    elif check_win(board, O):
        return -1
    else:
        return 0

# Minimax algorithm with alpha-beta pruning

def minimax(board, player, alpha, beta):
  
    # Evaluate the board if the game is over or the maximum depth has been reached
    
    if check_win(board, X) or check_win(board, O) or '-' not in [cell for row in board for cell in row]:
        return evaluate_board(board)
      
    # Maximizing player's turn
    
    if player == X:
        max_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = X
                    score = minimax(board, O, alpha, beta)
                    board[row][col] = EMPTY
                    max_score = max(max_score, score)
                    alpha = max(alpha, max_score)
                    if alpha >= beta:
                        break
            if alpha >= beta:
                break
        return max_score
      
    # Minimizing player's turn
    
    else:
        min_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = O
                    score = minimax(board, X, alpha, beta)
                    board[row][col] = EMPTY
                    min_score = min(min_score, score)
                    beta = min(beta, min_score)
                    if alpha >= beta:
                        break
            if alpha >= beta:
                break
        return min_score

# Function to make a move using the minimax algorithm with alpha-beta pruning

def make_move_alpha_beta(board, player):
    best_score = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = player
                score = minimax(board, O if player == X else X, -math.inf, math.inf)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    board[best_move[0]][best_move[1]] = player

# Minimax algorithm without pruning

def minimax_no_pruning(board, player):
  
    # Evaluate the board if the game
    
def evaluate_board(board):
if check_win(board, X):
return 1
elif check_win(board, O):
return -1
else:
return 0

def minimax_no_pruning(board, player):
  
# Evaluate the board if the game is over or the maximum depth has been reached

if check_win(board, X) or check_win(board, O) or '-' not in [cell for row in board for cell in row]:
return evaluate_board(board)

# Maximizing player's turn

if player == X:
max_score = -math.inf
for row in range(3):
for col in range(3):
if board[row][col] == EMPTY:
board[row][col] = X
score = minimax_no_pruning(board, O)
board[row][col] = EMPTY
max_score = max(max_score, score)
return max_score

# Minimizing player's turn

else:
min_score = math.inf
for row in range(3):
for col in range(3):
if board[row][col] == EMPTY:
board[row][col] = O
score = minimax_no_pruning(board, X)
board[row][col] = EMPTY
min_score = min(min_score, score)
return min_score

# Function to make a move using the minimax algorithm without pruning

def make_move_no_pruning(board, player):
best_score = -math.inf
best_move = None
for row in range(3):
for col in range(3):
if board[row][col] == EMPTY:
board[row][col] = player
score = minimax_no_pruning(board, O if player == X else X)
board[row][col] = EMPTY
if score > best_score:
best_score = score
best_move = (row, col)
board[best_move[0]][best_move[1]] = player

# Game loop

board = [[EMPTY for _ in range(3)] for _ in range(3)]
turn = X
print_board(board)
while True:
if turn == X:
make_move_alpha_beta(board, X)
else:
make_move_no_pruning(board, O)
print_board(board)
# Check if the game has ended
if check_win(board, turn):
print(turn + ' has won the game!')
break
elif '-' not in [cell for row in board for cell in row]:
print("It's a tie!")
break
# Switch to the other player
if turn == X:
turn = O
else:
turn = X
