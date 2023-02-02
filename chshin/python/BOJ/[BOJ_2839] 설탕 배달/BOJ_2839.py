N = int(input())

tmp = N // 5
flag = 0
for x in range(tmp, -1, -1):
    if (N - 5 * x) % 3 == 0:
        y = (N - 5 * x) // 3
        flag = 1
        break

print(x + y) if flag else print(-1)
