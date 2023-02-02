from collections import deque
import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
right = 10 ** 9

if A > B:
    print(-1)
elif A == B:
    print(1)
else:
    dq = deque()
    dq.append((A, 1))

    flag = 1
    while dq:
        tmp, cnt = dq.popleft()
        if tmp == B:
            print(cnt)
            flag = 0
            break

        if 2 * tmp <= right:
            dq.append((2 * tmp, cnt + 1))
        if 10 * tmp + 1 <= right:
            dq.append((10 * tmp + 1, cnt + 1))
    if flag:
        print(-1)