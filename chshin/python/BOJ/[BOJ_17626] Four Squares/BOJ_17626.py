"""
1 ~ 223
0 1 2 3 4 5 6 7 8 9 10 20
0 1 2 3 1 2 3 4 2 1 2
10-1
10-4
10-9
...
"""


from math import sqrt

n = int(input())
arr = [0]
for i in range(1, n + 1):
    if sqrt(i) == int(sqrt(i)):
        arr.append(1)
        continue

    tmp = 4
    for j in range(1, int(sqrt(i))+1):
        before = arr[i - j ** 2]
        if before < tmp:
            tmp = before
        if tmp == 1:
            break
    arr.append(tmp + 1)
print(arr[n])
