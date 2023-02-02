import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(p, q):
    pass
    dq = deque()
    dq.append([p, q])
    matrix2[p][q] = 1
    cnt = 1
    edges = set()
    while dq:
        r, c = dq.popleft()
        for d in range(4):
            nr, nc = r + drs[d], c + dcs[d]
            if 0 <= nr < N and 0 <= nc < M:
                if matrix1[nr][nc] != 0:
                    edges.add((nr, nc))
                elif matrix2[nr][nc] == 0:
                    dq.append([nr, nc])
                    matrix2[nr][nc] = 1
                    cnt += 1
    for r, c in edges:
        matrix1[r][c] += cnt



N, M = map(int, input().split())
matrix1 = [list(map(int, list(input()))) for _ in range(N)]
matrix2 = [[0] * M for _ in range(N)]
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

for r in range(N):
    for c in range(M):
        if matrix1[r][c] == 0 and matrix2[r][c] == 0:
            bfs(r, c)

for r in range(N):
    for c in range(M):
        matrix1[r][c] %= 10
    print(''.join(map(str, matrix1[r])))
