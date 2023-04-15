import math

X = 'X'
O = 'O'
EMPTY = '-'

# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    # No win found
    return False

# Function to evaluate the score of a board
def evaluate_board(board):
    if check_win(board, X):
        return 1
    elif check_win(board, O):
        return -1
    else:
        return 0

# Minimax algorithm with alpha-beta pruning
def minimax_alpha_beta(board, player, alpha, beta):
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
                    score = minimax_alpha_beta(board, O, alpha, beta)
                    board[row][col] = EMPTY
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return max_score
    # Minimizing player's turn
    else:
        min_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = O
                    score = minimax_alpha_beta(board, X, alpha, beta)
                    board[row][col] = EMPTY
                    min_score = min(min_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
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
                score = minimax_alpha_beta(board, O if player == X else X, -math.inf, math.inf)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    board[best_move[0]][best_move[1]] = player

# Minimax algorithm without alpha-beta pruning

def minimax(board, player):
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
                    score = minimax(board, O)
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
                    score = minimax(board, X)
                    board[row][col] = EMPTY
                    min_score = min(min_score, score)
        return min_score

# Function to make a move using the minimax algorithm without alpha-beta pruning
def make_move(board, player):
    best_score = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = player
                score = minimax(board, O if player == X else X)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    board[best_move[0]][best_move[1]] = player

# Main function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    player = X
    while not check_win(board, X) and not check_win(board, O) and '-' in [cell for row in board for cell in row]:
        print_board(board)
        if player == X:
            make_move_alpha_beta(board, player)
        else:
            make_move(board, player)
        player = O if player == X else X
    print_board(board)
    if check_win(board, X):
        print("X wins!")
    elif check_win(board, O):
        print("O wins!")
    else:
        print("Draw!")

# Play the game
play_game()
