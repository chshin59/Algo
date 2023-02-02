import sys
sys.stdin = open('input.txt')


def move(d, red, blue):
    # 두 공 중 더 앞에 있는 공 먼저 이동
    if [red[0] < blue[0], red[1] > blue[1], red[0] > blue[0], red[1] < blue[1]][d]:
        # red -> blue 이동
        while True:
            nr, nc = red[0] + drs[d], red[1] + dcs[d]
            if matrix[nr][nc] == '#':
                break
            elif matrix[nr][nc] == 'O':
                red = [-1, -1]
                break
            else:
                red = [nr, nc]
        while True:
            nr, nc = blue[0] + drs[d], blue[1] + dcs[d]
            if [nr, nc] == red or matrix[nr][nc] == '#':
                break
            elif matrix[nr][nc] == 'O':
                blue = [-1, -1]
                break
            else:
                blue = [nr, nc]
    else:
        # blue -> red 이동
        while True:
            nr, nc = blue[0] + drs[d], blue[1] + dcs[d]
            if matrix[nr][nc] == '#':
                break
            elif matrix[nr][nc] == 'O':
                blue = [-1, -1]
                break
            else:
                blue = [nr, nc]
        while True:
            nr, nc = red[0] + drs[d], red[1] + dcs[d]
            if [nr, nc] == blue or matrix[nr][nc] == '#':
                break
            elif matrix[nr][nc] == 'O':
                red = [-1, -1]
                break
            else:
                red = [nr, nc]
    return red, blue


def dfs(current_d, move_cnt, red, blue):
    global answer
    move_cnt += 1
    
    # cnt >= answer 이면 backtracking
    if move_cnt >= answer:
        return

    new_red, new_blue = move(current_d, red, blue)
    if new_blue == [-1, -1]:
        return
    if new_red == [-1, -1]:
        answer = move_cnt
        return

    # 3방향에 대해서
    for next_d in range(4):
        if current_d != next_d:
            dfs(next_d, move_cnt, new_red, new_blue)


N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]


# 공 위치
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 'B':
            matrix[r][c] = '.'
            blue = [r, c]
        elif matrix[r][c] == 'R':
            matrix[r][c] = '.'
            red = [r, c]

answer = 11
for d in range(4):
    dfs(d, 0, red, blue)
print(-1) if answer == 11 else print(answer)
