import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)
sys.stdin = open('input.txt')


def func(x, y):
    global color
    visited1[x][y] = 1
    for delta in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x2 = x + delta[0]
        y2 = y + delta[1]
        if 0 <= x2 < N and 0 <= y2 < N and not visited1[x2][y2]:
            if matrix[x2][y2] == color:
                func(x2, y2)


def func2(x, y):
    global color
    visited2[x][y] = 1
    for delta in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x2 = x + delta[0]
        y2 = y + delta[1]
        if 0 <= x2 < N and 0 <= y2 < N and not visited2[x2][y2]:
            if color == 'B' and matrix[x2][y2] == color:
                func2(x2, y2)
            elif color != 'B' and matrix[x2][y2] != 'B':
                func2(x2, y2)


N = int(input())
matrix = [list(input()) for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]

answer1 = 0
answer2 = 0
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            answer1 += 1
            color = matrix[i][j]
            func(i, j)
        if not visited2[i][j]:
            answer2 += 1
            color = matrix[i][j]
            func2(i, j)
print(answer1, answer2)
