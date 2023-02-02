# 9C2
# flag 사용

import sys
sys.stdin = open('input.txt')

lst = []
ssum = 0
for _ in range(9):
    tmp = int(input())
    ssum += tmp
    lst.append(tmp)

flag = 0
for i in range(9):
    for j in range(i + 1, 9):
        if ssum - (lst[i] + lst[j]) == 100:
            flag = 1
            del lst[j]
            del lst[i]
            break
    if flag == 1:
        break

for i in range(7):
    for j in range(i + 1, 7):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in range(7):
    print(lst[i])
