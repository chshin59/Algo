import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')


def tornado(r1, c1, d):
    sand = matrix[r1][c1]
    # 모래가 있다면
    if sand:
        matrix[r1][c1] = 0
        tmp = sand
        # 각각의 경우 모래를 더해줌
        for p, q, r, s, ratio in zip(x1, x2, x3, x4, ratios):
            r2 = r1 + drs[d]*p + drs[(d+1) % 4]*q + drs[(d+2) % 4]*r + drs[(d+3) % 4]*s
            c2 = c1 + dcs[d]*p + dcs[(d+1) % 4]*q + dcs[(d+2) % 4]*r + dcs[(d+3) % 4]*s
            tmp -= int(sand * ratio)
            if 0 <= r2 < N and 0 <= c2 < N:
                matrix[r2][c2] += int(sand * ratio)
        r2 = r1 + drs[d]
        c2 = c1 + dcs[d]
        if 0 <= r2 < N and 0 <= c2 < N:
            matrix[r2][c2] += tmp


N = int(input())
r, c = (N // 2, N // 2)
direction = 3

# 서:0 남:1 동:2 북:3
drs = [0, 1, 0, -1]
dcs = [-1, 0, 1, 0]

x1 = [2, 1, 0, 0, 0, 0, 0, 0, 1]
x2 = [0, 1, 1, 2, 1, 0, 0, 0, 0]
x3 = [0, 0, 0, 0, 1, 1, 0, 0, 0]
x4 = [0, 0, 0, 0, 0, 1, 1, 2, 1]
ratios = [0.05, 0.1, 0.07, 0.02, 0.01, 0.01, 0.07, 0.02, 0.1]

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
answer = sum(map(sum, matrix))

for i in range(1, 2 * N):
    direction = (direction + 1) % 4
    for j in range(-(-i // 2)):
        if j < N-1:
            r += drs[direction]
            c += dcs[direction]
            tornado(r, c, direction)
answer -= sum(map(sum, matrix))
print(answer)
