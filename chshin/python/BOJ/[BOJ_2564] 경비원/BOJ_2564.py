import sys

sys.stdin = open('input.txt')

x, y = map(int, input().split())
N = int(input())
lst = []
for _ in range(N + 1):
    p, q = map(int, input().split())
    if p == 1:
        lst.append(q)
    elif p == 2:
        lst.append(2 * x + y - q)
    elif p == 3:
        lst.append(2 * x + 2 * y - q)
    elif p == 4:
        lst.append(x + q)

position = lst[-1]
lst = lst[:-1]

for i in range(N):
    tmp = lst[i]
    lst[i] = min(2 * x + 2 * y - abs(position - tmp), abs(position - tmp))
print(sum(lst))
