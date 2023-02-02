import sys
sys.stdin = open('input.txt')


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    cost[a][b] = l
    cost[b][a] = l

for k in range(1, n + 1):
    cost[k][k] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])


answer = 0
for row in cost[1:]:
    tmp = 0
    for col in range(1, n + 1):
        if row[col] <= m:
            tmp += items[col]
    if tmp > answer:
        answer = tmp
print(answer)