import sys
from collections import deque

sys.stdin = open('input.txt')


def func():
    global answer, visits

    while visits and not visited[N - 1][M - 1]:
        for _ in range(len(visits)):
            r, c, cnt = visits.popleft()

            if cnt:
                for d in range(4):
                    new_r, new_c, new_cnt = r + drs[d], c + dcs[d], cnt
                    if 0 <= new_r < N and 0 <= new_c < M and visited[new_r][new_c] != 2:
                        if matrix[new_r][new_c]:
                            visits.append((new_r, new_c, new_cnt - 1))
                        else:
                            visits.append((new_r, new_c, new_cnt))
                        visited[new_r][new_c] = 2

            else:
                for d in range(4):
                    new_r, new_c, new_cnt = r + drs[d], c + dcs[d], cnt
                    if 0 <= new_r < N and 0 <= new_c < M and not visited[new_r][new_c]:
                        if matrix[new_r][new_c] == 0:
                            visits.append((new_r, new_c, new_cnt))
                            visited[new_r][new_c] = 1
        answer += 1

    if visited[N - 1][M - 1]:
        return answer
    else:
        return -1


N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

answer = 1
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]
visits = deque()
visits.append((0, 0, 1))
visited[0][0] = 2

print(func())
