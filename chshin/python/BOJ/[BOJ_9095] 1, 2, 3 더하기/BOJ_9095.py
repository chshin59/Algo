import sys
sys.stdin = open('input.txt')


def func(n):
    answer_lst = [0, 1, 2, 4]
    for i in range(4, n + 1):
        answer_lst.append(answer_lst[i-1] + answer_lst[i-2] + answer_lst[i-3])
    return answer_lst[n]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    print(func(n))
