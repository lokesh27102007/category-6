def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def minimax(board, is_max):
    if check_winner(board, "X"):
        return 1

    if check_winner(board, "O"):
        return -1

    if " " not in board:
        return 0

    if is_max:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, False))
                board[i] = " "

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, True))
                board[i] = " "

        return best


board = [
    "X", "O", "X",
    "O", "X", " ",
    " ", " ", "O"
]

best_score = -100
best_move = -1

for i in range(9):
    if board[i] == " ":
        board[i] = "X"
        score = minimax(board, False)
        board[i] = " "

        if score > best_score:
            best_score = score
            best_move = i

print("Best position:", best_move + 1)
print("Best score:", best_score)
