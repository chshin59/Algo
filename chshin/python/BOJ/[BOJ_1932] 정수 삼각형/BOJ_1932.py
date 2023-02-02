import sys
sys.stdin = open('input.txt')

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

for r in range(1, N):
    triangle[r][0] += triangle[r - 1][0]
    triangle[r][r] += triangle[r - 1][r - 1]
    for c in range(1, r):
        triangle[r][c] += max(triangle[r-1][c-1], triangle[r-1][c])

print(max(triangle[-1]))