import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')


def dfs(r, c):
    global visited, ssum
    ssum += matrix[r][c]
    visited[r][c] = 1
    unions.append((r, c))
    # 4방향에 대해서 차이가 두 값 사이면 장소 저장
    for d in range(4):
        nr, nc = r + drs[d], c + dcs[d]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if L <= abs(matrix[nr][nc] - matrix[r][c]) <= R:
                dfs(nr, nc)


N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

flag = 1
answer = -1
while flag:
    flag = 0
    answer += 1
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(r % 2, N, 2):
            if not visited[r][c]:
                unions = []
                ssum = 0
                dfs(r, c)

                # unions = [(r, c), (r, c), ...]
                if len(unions) > 1:
                    flag = 1
                    tmp = ssum // len(unions)
                    for union in unions:
                        matrix[union[0]][union[1]] = tmp

print(answer)