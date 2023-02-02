import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def func(num):
    for i in tree[num]:
        if not visited[i]:
            parent[i] = num
            visited[i] = 1
            func(i)


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q = map(int, input().split())
    tree[p].append(q)
    tree[q].append(p)

parent = [0] * (N + 1)
visited = [0] * (N + 1)
visited[1] = 1
func(1)
for i in range(2, N + 1):
    print(parent[i])

