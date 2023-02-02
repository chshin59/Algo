import sys
sys.stdin = open('input.txt')

V = int(input())
N = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(N):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [1]
idx = 0
while idx < len(visited):
    for i in graph[visited[idx]]:
        if i not in visited:
            visited.append(i)
    idx += 1
print(len(visited)-1)
