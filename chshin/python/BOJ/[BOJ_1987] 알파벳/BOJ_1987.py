import sys
sys.stdin = open('input.txt')


def dfs(r, c, cnt):
    global answer

    answer = max(answer, cnt)

    for d in range(4):
        nr = r + drs[d]
        nc = c + dcs[d]

        if 0 <= nr < R and 0 <= nc < C:
            tmp = ord(matrix[nr][nc]) - 65
            if not visited[tmp]:
                visited[tmp] = 1
                dfs(nr, nc, cnt + 1)
                visited[tmp] = 0


R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]
visited = [0] * 26
visited[ord(matrix[0][0]) - 65] = 1
answer = 1
dfs(0, 0, 1)
print(answer)