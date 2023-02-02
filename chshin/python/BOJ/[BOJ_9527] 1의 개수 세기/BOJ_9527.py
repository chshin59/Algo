import sys
sys.stdin = open('input.txt')


def func(N):
    if N == 0:
        return 0

    cnt = -1
    tmp = 1
    while tmp <= N:
        tmp *= 2
        cnt += 1

    N2 = 2 ** cnt
    if N == N2:
        return int(cnt * (2 ** (cnt - 1)) + 1)
    else:
        return func(N2) + func(N - N2) + N - N2


A, B = map(int, input().split())
print(func(B) - func(A-1))
