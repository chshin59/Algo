import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

for r in range(1, N):
    matrix[r][0] += min(matrix[r-1][1], matrix[r-1][2])
    matrix[r][1] += min(matrix[r-1][2], matrix[r-1][0])
    matrix[r][2] += min(matrix[r-1][0], matrix[r-1][1])
print(min(matrix[-1]))
