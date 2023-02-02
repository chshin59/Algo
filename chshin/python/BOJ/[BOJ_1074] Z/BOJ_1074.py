import sys

sys.stdin = open('input.txt')


# 재귀
def func(N, r, c):
    if N == 1:
        matrix = [[0, 1], [2, 3]]
        return matrix[r][c]
    else:
        half = 2 ** (N - 1)
        if r >= 2 ** (N - 1):
            if c >= half:
                return func(N - 1, r - half, c - half) + 3 * (half ** 2)
            else:
                return func(N - 1, r - half, c) + 2 * (half ** 2)
        else:
            if c >= half:
                return func(N - 1, r, c - half) + half ** 2
            else:
                return func(N - 1, r, c)


N, r, c = map(int, input().split())
print(func(N, r, c))
