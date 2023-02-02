from collections import deque
import sys
sys.stdin = open('input.txt')


def check(i, j):
    if not matrix2[i][j]:
        return False

    cnt = 1
    i2 = i
    while i2 >= 1 and matrix2[i2 - 1][j]:
        cnt += 1
        i2 -= 1

    i2 = i
    while i2 <= 5 and matrix2[i2 + 1][j]:
        cnt += 1
        i2 += 1

    if cnt == matrix2[i][j]:
        return True

    cnt = 1
    j2 = j
    while j2 >= 1 and matrix2[i][j2 - 1]:
        cnt += 1
        j2 -= 1

    j2 = j
    while j2 <= 5 and matrix2[i][j2 + 1]:
        cnt += 1
        j2 += 1

    if cnt == matrix2[i][j]:
        return True
    return False



def func():
    while True:
        explodes = []
        # check
        for i in range(7):
            for j in range(7):
                if check(i, j):
                    explodes.append([i, j])

        if not explodes:
            break

        for i, j in explodes:
            # explode
            matrix2[i][j] = 0

            # down
            dq = deque()
            for i2 in range(i - 1, -1, -1):
                if matrix2[i2][j]:
                    dq.append(matrix2[i2][j])
            dq.extend([0, 0, 0, 0, 0, 0, 0])

            for i2 in range(i, -1, -1):
                matrix2[i2][j] = dq.popleft()


matrix = [list(map(int, input().split())) for _ in range(7)]
ball = int(input())

drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

answer = 49
for c in range(7):
    matrix2 = [row[:] for row in matrix]

    for r in range(6, -1, -1):
        if not matrix2[r][c]:
            matrix2[r][c] = ball
            break

    func()

    cnt = 0
    for i in range(7):
        for j in range(7):
            if matrix2[i][j]:
                cnt += 1
    answer = min(answer, cnt)
print(answer)
