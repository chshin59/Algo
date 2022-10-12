from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def func(k, video):
    visited = [0] * (N + 1)
    visited[video] = 1
    dq = deque()
    dq.append(video)
    cnt = 0
    while dq:
        tmp = dq.popleft()
        for v, usado in tree[tmp]:
            if not visited[v] and usado >= k:
                visited[v] = 1
                dq.append(v)
                cnt += 1
    print(cnt)


N, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    tree[p].append((q, r))
    tree[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    func(k, v)
