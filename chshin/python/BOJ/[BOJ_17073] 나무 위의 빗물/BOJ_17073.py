import sys
input = sys.stdin.readline

N, W = map(int, input().split())
count = [0] * (N + 1)
tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cnt = 0
for node in range(2, N + 1):
    if len(tree[node]) == 1:
        cnt += 1
print(W / cnt)
