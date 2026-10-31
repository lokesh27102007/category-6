def minimax(board, is_max):
    if "X" in board and board.count("X") == 3:
        return 1

    if "O" in board and board.count("O") == 3:
        return -1

    if " " not in board:
        return 0

    if is_max:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best = min(best, score)

        return best

board = ["X", "O", "X",
         "O", "X", " ",
         " ", " ", "O"]

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
