from math import prod
n, m = map(int, input().split())
m = min(m, n - m)

A = prod(range(n - m + 1, n + 1))
B = prod(range(1, m + 1))
print(A // B)