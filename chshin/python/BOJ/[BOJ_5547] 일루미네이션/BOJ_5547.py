import sys
sys.setrecursionlimit(20000)


def dfs(w, h):
    global visited
    visited[h][w] = 1

    for d in range(6):
        if h % 2:
            w2, h2 = w + delta_w[d], h + delta_h[d]
        else:
            w2, h2 = w + delta_w2[d], h + delta_h[d]
        if 0 <= w2 < W and 0 <= h2 < H:
            if not matrix[h2][w2] and not visited[h2][w2]:
                dfs(w2, h2)


def func(w, h):
    global answer
    answer += 6

    for d in range(6):
        if h % 2:
            w2, h2 = w + delta_w[d], h + delta_h[d]
        else:
            w2, h2 = w + delta_w2[d], h + delta_h[d]
        if 0 <= w2 < W and 0 <= h2 < H and matrix[h2][w2]:
            answer -= 1


W, H = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]
answer = 0

delta_w = [-1, 0, 1, 0, -1, -1]
delta_w2 = [0, 1, 1, 1, 0, -1]
delta_h = [-1, -1, 0, 1, 1, 0]

visited = [[0] * W for _ in range(H)]

for h in [0, H - 1]:
    for w in range(W):
        if not matrix[h][w]:
            dfs(w, h)

for h in range(1, H - 1):
    for w in [0, W - 1]:
        if not matrix[h][w]:
            dfs(w, h)

for h in range(H):
    for w in range(W):
        if not visited[h][w] and not matrix[h][w]:
            matrix[h][w] = 1

for h in range(H):
    for w in range(W):
        if matrix[h][w]:
            func(w, h)

print(answer)
