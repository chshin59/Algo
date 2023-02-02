import sys
sys.stdin = open('input.txt')


def move(shark):
    r, c, s, d, z = shark
    # 위
    if d == 1:
        if r > s:
            r = r - s
        elif r <= s < r + R - 1:
            d = 2
            r = s - r
        else:
            r = r + 2 * R - 2 - s
    # 아래
    elif d == 2:
        if s < R - 1 - r:
            r = r + s
        elif R - 1 - r <= s < 2 * R - 2 - r:
            d = 1
            r = 2 * R - 2 - r - s
        else:
            r = r + s - 2 * R + 2
    # 오른쪽
    elif d == 3:
        if s < C - 1 - c:
            c = c + s
        elif C - 1 - c <= s < 2 * C - 2 - c:
            d = 4
            c = 2 * C - 2 - c - s
        else:
            c = c + s - 2 * C + 2
    # 왼쪽
    else:
        if c > s:
            c = c - s
        elif c <= s < c + C - 1:
            d = 3
            c = s - c
        else:
            c = c + 2 * C - 2 - s

    # 4. 같은 위치에 있는 상어 처리
    if (r, c) not in shark_positions:
        shark_positions.add((r, c))
        moved_sharks.append([r, c, s, d, z])
        matrix[r][c] = z


R, C, M = map(int, input().split())
matrix = [[0] * C for _ in range(R)]
sharks = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    matrix[r-1][c-1] = z
    if d <= 2:
        s %= 2 * (R - 1)
    else:
        s %= 2 * (C - 1)
    sharks.append([r-1, c-1, s, d, z])
sharks.sort(key=lambda x: x[-1], reverse=True)

answer = 0
# 1. 낚시왕 이동
for c in range(C):
    for r in range(R):
        # 2. 낚시
        if matrix[r][c]:
            answer += matrix[r][c]
            matrix[r][c] = 0
            break

    moved_sharks = []
    shark_positions = set()
    for shark in sharks:
        matrix[shark[0]][shark[1]] = 0

    for shark in sharks:
        # 낚시한 상어 sharks에서 제거
        if (shark[0], shark[1]) != (r, c):
            # 3. 상어 이동
            move(shark)
    sharks = moved_sharks

print(answer)