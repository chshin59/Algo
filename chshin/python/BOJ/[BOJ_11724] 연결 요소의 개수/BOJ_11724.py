import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def DFS(x):
    visited.append(x)
    for v in graph[x]:
        if v not in visited:
            DFS(v)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = []
answer = 0

for i in range(1, N+1):
    if i not in visited:
        answer += 1
        DFS(i)

print(answer)
