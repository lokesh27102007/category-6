def alphabeta(depth, node, alpha, beta, is_max):
    if depth == 2:
        return node

    if is_max:
        best = float('-inf')

        for value in node:
            best = max(
                best,
                alphabeta(depth + 1, value, alpha, beta, False)
            )
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for value in node:
            best = min(
                best,
                alphabeta(depth + 1, value, alpha, beta, True)
            )
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

chess_moves = [[3, 5], [2, 9]]

result = alphabeta(
    0, chess_moves, float('-inf'), float('inf'), True
)

print("Best evaluation:", result)
