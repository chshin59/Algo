# 5
# 2 3 1 6 5 4
# 3 1 2 4 6 5
# 5 6 4 1 3 2
# 1 3 6 2 4 5
# 4 1 6 5 2 3

# 24/ 36/ 15
# 35/ 14/ 26
# 52/ 61/ 43
# 15/ 32/ 64
# 43/ 15/ 62

# 숫자 1개를 선택하면 그 이후는 자동적으로 결정!!
# 1부터 6까지 각각의 경우
# 남은 숫자 중 최대값의 합을 구하고
# 그 중 최대인 경우를 선택
# 숫자 -> index -> index -> 숫자 / += 최대값

import sys

sys.stdin = open('input.txt')


def my_index(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i


def func(dices, select_num):
    total = 0
    num1 = select_num
    idx_to_idx = [5, 3, 4, 1, 2, 0]

    for dice in dices:
        idx = my_index(dice, num1)
        num2 = dice[idx_to_idx[idx]]

        if {num1, num2} == {5, 6}:
            total += 4
        elif num1 == 6 or num2 == 6:
            total += 5
        else:
            total += 6

        num1 = num2

    return total


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for num in range(1, 7):
    if func(dices, num) > answer:
        answer = func(dices, num)

print(answer)
