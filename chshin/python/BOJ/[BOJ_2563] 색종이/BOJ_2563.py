import sys
sys.stdin = open('input.txt')

N = int(input())
matrix = [[0] * 100 for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            matrix[i][j] = 1

total = 0
for i in range(100):
    for j in range(100):
        total += matrix[i][j]
print(total)
