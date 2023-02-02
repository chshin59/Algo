import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
r, c, d = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
new_r = new_c = -1

while True:
    matrix[r][c] = 2
    for _ in range(4):
        d = (d + 3) % 4
        new_r, new_c = r + drs[d], c + dcs[d]
        if matrix[new_r][new_c] == 0:
            r, c = new_r, new_c
            break
    else:
        d = (d + 2) % 4
        new_r, new_c = r + drs[d], c + dcs[d]
        if matrix[new_r][new_c] == 1:
            break
        else:
            d = (d + 2) % 4
            r, c = new_r, new_c

answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            answer += 1
print(answer)
