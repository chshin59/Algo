import sys

sys.stdin = open('input.txt')


def my_min(lst):
    value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < value:
            value = lst[i]
    return value


def my_max(lst):
    value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > value:
            value = lst[i]
    return value


def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


N = int(input())
poles = []
for _ in range(N):
    poles.append(list(map(int, input().split())))

tmp = [poles[i][0] for i in range(N)]
s_idx = my_min(tmp)

for i in range(N):
    poles[i][0] -= s_idx

# 빈 리스트 생성
polygon = [0 for i in range(my_min(tmp), my_max(tmp) + 1)]

for i in range(N):
    for j in range(i+1, N):
        if poles[i][1] < poles[j][1]:
            poles[i], poles[j] = poles[j], poles[i]

# 1
# 가장 높은 기둥 탐색
# idx에 높이 입력
polygon[poles[0][0]] = poles[0][1]
L = R = poles[0][0]

# 2
# 기둥이 높은 순으로 다각형에 추가
# 창고가 모든 영역을 표함할 때까지 반복
for pole in poles[1:]:
    if pole[0] < L:
        for i in range(pole[0], L):
            polygon[i] = pole[1]
        L = pole[0]
    elif pole[0] > R:
        for i in range(pole[0], R, -1):
            polygon[i] = pole[1]
        R = pole[0]

    if 0 not in polygon:
        break

print(my_sum(polygon))
