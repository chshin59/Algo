"""
Dijkstra(s, A, D):
    U = {s}

    for 모든 정점 v
        D[v] <- A[s][v]

    while U != V:
        D[w]가 최소인 정점 w in V-U 를 선택
        U <- U | {w}

        for w에 인접한 모든 정점 v
            D[v] <- min(D[v], D[w] + A[w][v])
"""
import sys
sys.stdin = open('input.txt')


def Dijkstra(s):
    D = [float('inf') for _ in range(n + 1)]

    U = {s}
    D[s] = 0

    for v in range(1, n + 1):
        if matrix[s][v]:
            D[v] = matrix[s][v]

    while len(U) != n:
        tmp = float('inf')
        for i in set(range(1, n + 1)) - U:
            if D[i] < tmp:
                w = i
                tmp = D[i]
        
        U = U | {w}

        for v in range(1, n + 1):
            if matrix[w][v]:
                D[v] = min(D[v], D[w] + matrix[w][v])
    
    result = 0
    for v in range(1, n + 1):
        if D[v] <= m:
            result += items[v]
    return result


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    matrix[a][b] = l
    matrix[b][a] = l

answer = 0
for s in range(1, n + 1):
    tmp = Dijkstra(s)
    if tmp > answer:
        answer = tmp
print(answer)