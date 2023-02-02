from collections import deque


def bfs(i, j):
    visited = [1] + [0 for _ in range(N)]
    dq = deque([i, j])
    visited[i] = visited[j] = 1
    cnt = ssum = 0
    while visited != [1] * (N + 1):
        cnt += 1
        for _ in range(len(dq)):
            tmp = dq.popleft()
            for k in tree[tmp]:
                if not visited[k]:
                    ssum += cnt
                    visited[k] = 1
                    dq.append(k)
    return 2 * ssum


N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(M):
    p, q = map(int, input().split())
    tree[p].append(q)
    tree[q].append(p)

distance = float('inf')
for i in range(1, N):
    for j in range(i + 1, N + 1):
        tmp = bfs(i, j)
        if tmp < distance:
            p, q, distance = i, j, tmp
print(p, q, distance)
