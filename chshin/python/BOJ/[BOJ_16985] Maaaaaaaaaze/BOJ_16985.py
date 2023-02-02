from itertools import permutations
from collections import deque
import sys
sys.stdin = open('input.txt')


def rotate(maze, idx):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[j][4 - i] = maze[idx][i][j]
    maze[idx] = tmp


def escape():
    global answer

    # 시작지점, 끝지점
    if not maze[0][0][0] or not maze[4][4][4]:
        return

    dq = deque()
    dq.append([0, 0, 0, 0])
    visited = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] for _ in range(5)]

    # BFS
    while dq:
        # floor, row, col, cnt
        f, r, c, cnt = dq.popleft()
        if (f, r, c) == (4, 4, 4):
            answer = min(answer, cnt)
            break

        visited[f][r][c] = 1
        for d in range(6):
            nf = f + dfs[d]
            nr = r + drs[d]
            nc = c + dcs[d]
            if 0 <= nf < 5 and 0 <= nr < 5 and 0 <= nc < 5:
                if maze[nf][nr][nc] and not visited[nf][nr][nc]:
                    dq.append([nf, nr, nc, cnt + 1])


maze_input = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

dfs = [-1, 1, 0, 0, 0, 0]
drs = [0, 0, -1, 1, 0, 0]
dcs = [0, 0, 0, 0, -1, 1]

answer = 126
for maze in permutations(maze_input, 5):
    maze = list(maze)
    for i in range(1, 1025):
        if i % 1 == 0:
            rotate(maze, 0)
        if i % 4 == 0:
            rotate(maze, 1)
        if i % 16 == 0:
            rotate(maze, 2)
        if i % 64 == 0:
            rotate(maze, 3)
        if i % 256 == 0:
            rotate(maze, 4)

        escape()
        if answer == 12:
            break
    if answer == 12:
        break

print(-1 if answer == 126 else answer)
