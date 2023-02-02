import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def find(c):
    p = parent[c]
    if p == c:
        return p
    return find(p)


def union(p, q):
    if p < q:
        parent[q] = p
    else:
        parent[p] = q


N, M = map(int, input().split())
parent = list(map(int, range(N)))
for i in range(1, M + 1):
    p, q = map(int, input().split())
    pp = find(p)
    qq = find(q)
    if pp == qq:
        print(i)
        break
    union(pp, qq)
else:
    print(0)
