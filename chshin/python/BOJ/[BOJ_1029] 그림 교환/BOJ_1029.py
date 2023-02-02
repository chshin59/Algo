from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
matrix = [list(map(int, list(input()))) for _ in range(N)]
dp = [[float('inf')] * N for _ in range(2 ** N)]

dq = deque()
dq.append([0, 1, 0])
while dq:
    for _ in range(len(dq)):
        i, owners, price = dq.popleft()

        for j in range(N):
            if not (1 << j) & owners and matrix[i][j] >= price:
                if dp[owners + (1 << j)][j] > matrix[i][j]:
                    dp[owners + (1 << j)][j] = matrix[i][j]
                    dq.append([j, owners + (1 << j), matrix[i][j]])

print(bin(owners).count('1'))
