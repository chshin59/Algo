import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0] * (N + 1)]
for _ in range(N):
    matrix.append([0] + list(map(int, input().split())))

for r in range(1, N + 1):
    for c in range(1, N + 1):
        matrix[r][c] += matrix[r-1][c] + matrix[r][c-1] - matrix[r-1][c-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix[x2][y2] - matrix[x2][y1-1] - matrix[x1-1][y2] + matrix[x1-1][y1-1])
