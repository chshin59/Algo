import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def func(prev_node, total):
    for node, dist in tree[prev_node]:
        if not visited[node]:
            visited[node] = 1
            answer[node] = total + dist
            func(node, total + dist)
            visited[node] = 0


V = int(input())
tree = [[] for _ in range(V + 1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1, 2):
        tree[arr[0]].append((arr[i], arr[i + 1]))

visited = [0] * (V + 1)
visited[1] = 1
answer = [0] * (V + 1)
func(1, 0)
tmp = answer.index(max(answer))

visited = [0] * (V + 1)
visited[tmp] = 1
answer = [0] * (V + 1)
func(tmp, 0)
print(max(answer))
