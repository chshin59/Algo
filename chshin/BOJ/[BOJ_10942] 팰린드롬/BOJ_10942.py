import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

matrix = [[0] * N for _ in range(N)]
for i in range(N):
    matrix[i][i] = 1
for i in range(N - 1):
    matrix[i][i + 1] = int(arr[i] == arr[i + 1])

for j in range(2, N):
    for k in range(N - j):
        if matrix[k+1][j+k-1] and arr[k] == arr[j + k]:
            matrix[k][j+k] = 1
        else:
            matrix[k][j + k] = 0

for _ in range(M):
    S, E = map(int, input().split())
    print(matrix[S-1][E-1])
