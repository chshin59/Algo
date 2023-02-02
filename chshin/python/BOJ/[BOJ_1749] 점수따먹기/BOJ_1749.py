import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [[0] * (M+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        matrix2[r][c] = matrix[r-1][c-1] + matrix2[r][c-1] + matrix2[r-1][c] - matrix2[r-1][c-1]

answer = float('-inf')
for r1 in range(1, N + 1):
    for r2 in range(r1, N + 1):
        for c1 in range(1, M + 1):
            for c2 in range(c1, M + 1):
                tmp = matrix2[r2][c2] - matrix2[r2][c1-1] - matrix2[r1-1][c2] + matrix2[r1-1][c1-1]
                if tmp > answer:
                    answer = tmp
print(answer)
