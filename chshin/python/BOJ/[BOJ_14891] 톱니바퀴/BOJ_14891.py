from collections import deque
import sys
sys.stdin = open('input.txt')


def rotate(num, d):
    if d == 1:
        tmp = wheels[num].pop()
        wheels[num].appendleft(tmp)
    elif d == -1:
        tmp = wheels[num].popleft()
        wheels[num].append(tmp)
    return


wheels = [0] + [deque(list(map(int, list(input())))) for _ in range(4)]
K = int(input())
for _ in range(K):
    num, d = map(int, input().split())
    rotates = [0, 0, 0, 0, 0]

    rotates[num] = d
    tmp_d = d
    for i in range(num - 1, 0, -1):
        if wheels[i][2] == wheels[i + 1][6]:
            break
        else:
            tmp_d *= -1
            rotates[i] = tmp_d
    tmp_d = d
    for j in range(num + 1, 5):
        if wheels[j - 1][2] == wheels[j][6]:
            break
        else:
            tmp_d *= -1
            rotates[j] = tmp_d
    for i in range(1, 5):
        rotate(i, rotates[i])

answer = 0
for i in range(4):
    answer += wheels[i + 1][0] * (2 ** i)
print(answer)