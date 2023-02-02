import sys
sys.stdin = open('input.txt')


def is_palindrome(l, r):
    for i in range(l, (l + r) // 2 + 1):
        if string[i] != string[r + l - i]:
            return False
    return True


string = input()
N = len(string)
matrix = [[0] * N for _ in range(N)]

for c in range(1, N - 1):
    l, r = c - 1, c + 1
    while 0 <= l and r < N:
        if is_palindrome(l, r):
            matrix[l][r] = 1
            l -= 1
            r += 1
        else:
            break

for l in range(N - 1):
    r = l + 1
    while 0 <= l and r < N:
        if is_palindrome(l, r):
            matrix[l][r] = 1
            l -= 1
            r += 1
        else:
            break

DP = [1] * N
for r in range(1, N):
    DP[r] = DP[r - 1] + 1
    for l in range(r):
        if matrix[l][r]:
            if l == 0:
                DP[r] = 1
            else:
                DP[r] = min(DP[l - 1] + 1, DP[r])
print(DP[-1])
