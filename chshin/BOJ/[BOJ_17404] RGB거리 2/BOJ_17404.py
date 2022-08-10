import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

cost = [[float('inf')] * 3 for _ in range(3)]
for i in range(3):
    cost[i][i] = matrix[0][i]

for n in range(1, N):
    tmp = [[float('inf')] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tmp_list = []
            for k in range(3):
                if j != k:
                    tmp_list.append(cost[i][k])
            tmp[i][j] = min(tmp_list) + matrix[n][j]
    cost = tmp[:]

answer = float('inf')
for i in range(3):
    for j in range(3):
        if i != j:
            answer = min(answer, cost[i][j])
print(answer)