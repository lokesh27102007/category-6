def minimax(depth, node, is_max):
    if depth == 2:
        return node

    if is_max:
        return max(
            minimax(depth + 1, value, False)
            for value in node
        )
    else:
        return min(
            minimax(depth + 1, value, True)
            for value in node
        )

chess_moves = [[3, 5], [2, 9]]

best_move = minimax(0, chess_moves, True)

print("Best evaluation for chess:", best_move)
