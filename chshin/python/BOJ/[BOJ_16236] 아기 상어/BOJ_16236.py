import sys
from collections import deque
sys.stdin = open('input.txt')


def move():
    global position
    visited = [[0] * N for _ in range(N)]
    visited[position[0]][position[1]] = 1

    visits = deque()
    visits.append(position)

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    prey = []
    distance = 0

    while not prey and len(visits):
        for _ in range(len(visits)):
            tmp = visits.popleft()
            for k in range(4):
                x2, y2 = tmp[0] + dxs[k], tmp[1] + dys[k]
                if 0 <= x2 < N and 0 <= y2 < N and not visited[x2][y2]:
                    if matrix[x2][y2] == 0 or matrix[x2][y2] == size:
                        visits.append([x2, y2])
                    elif matrix[x2][y2] < size:
                        prey.append([x2, y2])
                    visited[x2][y2] = 1
        distance += 1
    if prey:
        prey.sort()
        position = prey[0]
        matrix[position[0]][position[1]] = 0
        return distance


N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

for x in range(N):
    for y in range(N):
        if matrix[x][y] == 9:
            position = [x, y]
            matrix[x][y] = 0
            break

answer = 0
count = 0
size = 2
while True:
    d = move()
    if d is None:
        break
    else:
        answer += d
        count += 1
        if count == size:
            size += 1
            count = 0
print(answer)
