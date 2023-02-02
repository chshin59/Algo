from itertools import combinations
import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

stores = []
houses = []

for r in range(N):
    for c in range(N):
        if matrix[r][c] == 1:
            houses.append([r, c])
        elif matrix[r][c] == 2:
            stores.append([r, c])

K = len(stores)
answer = float('INF')
for selected_stores in combinations(stores, M):
    tmp1 = 0
    for house in houses:
        tmp2 = float('INF')
        for selected_store in selected_stores:
            chicken_distance = abs(house[0] - selected_store[0]) + abs(house[1] - selected_store[1])
            if chicken_distance < tmp2:
                tmp2 = chicken_distance
        tmp1 += tmp2
    if tmp1 < answer:
        answer = tmp1
print(answer)
