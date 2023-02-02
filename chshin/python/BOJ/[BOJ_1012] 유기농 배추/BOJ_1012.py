import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
# sys.stdin = open('input.txt')


def dfs(x, y):
    matrix[x][y] = 0
    for k in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x2 = x + k[0]
        y2 = y + k[1]
        if 0 <= x2 <= M-1 and 0 <= y2 <= N-1 and matrix[x2][y2] == 1:
            dfs(x2, y2)


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        p, q = map(int, input().split())
        matrix[p][q] = 1

    answer = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                answer += 1
                dfs(i, j)
    print(answer)
