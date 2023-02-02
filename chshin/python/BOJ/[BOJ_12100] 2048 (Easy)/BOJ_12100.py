import sys
sys.stdin = open('input.txt')


def dfs(board, cnt):
    global answer
    if cnt == 5:
        answer = max(answer, max(map(max, board)))
        return

    # up
    new_board = [[0] * N for _ in range(N)]
    for c in range(N):
        new_board[0][c] = board[0][c]
        i, j = 0, c
        for r in range(1, N):
            if board[r][c]:
                if new_board[i][j] == board[r][c]:
                    new_board[i][j] *= 2
                    i += 1
                elif new_board[i][j]:
                    new_board[i + 1][j] = board[r][c]
                    i += 1
                else:
                    new_board[i][j] = board[r][c]
    dfs(new_board, cnt + 1)

    # down
    new_board = [[0] * N for _ in range(N)]
    for c in range(N):
        new_board[N - 1][c] = board[N - 1][c]
        i, j = N - 1, c
        for r in range(N - 2, -1, -1):
            if board[r][c]:
                if new_board[i][j] == board[r][c]:
                    new_board[i][j] *= 2
                    i -= 1
                elif new_board[i][j]:
                    new_board[i - 1][j] = board[r][c]
                    i -= 1
                else:
                    new_board[i][j] = board[r][c]
    dfs(new_board, cnt + 1)

    # left
    new_board = [[0] * N for _ in range(N)]
    for r in range(N):
        new_board[r][0] = board[r][0]
        i, j = r, 0
        for c in range(1, N):
            if board[r][c]:
                if new_board[i][j] == board[r][c]:
                    new_board[i][j] *= 2
                    j += 1
                elif new_board[i][j]:
                    new_board[i][j + 1] = board[r][c]
                    j += 1
                else:
                    new_board[i][j] = board[r][c]
    dfs(new_board, cnt + 1)

    # right
    new_board = [[0] * N for _ in range(N)]
    for r in range(N):
        new_board[r][N - 1] = board[r][N - 1]
        i, j = r, N - 1
        for c in range(N - 2, -1, -1):
            if board[r][c]:
                if new_board[i][j] == board[r][c]:
                    new_board[i][j] *= 2
                    j -= 1
                elif new_board[i][j]:
                    new_board[i][j - 1] = board[r][c]
                    j -= 1
                else:
                    new_board[i][j] = board[r][c]
    dfs(new_board, cnt + 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(board, 0)
print(answer)