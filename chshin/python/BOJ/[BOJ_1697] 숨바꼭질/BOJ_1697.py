import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, input().split())

# BFS
position_list = deque()
position_list.append(N)
visited = {N}

cnt = 0
if N <= K:
    while K not in position_list:
        l = len(position_list)
        for _ in range(l):
            tmp = position_list.popleft()
            if tmp - 1 not in visited and 0 <= tmp - 1 <= 100000:
                position_list.append(tmp - 1)
            if tmp + 1 not in visited and 0 <= tmp + 1 <= 100000:
                position_list.append(tmp + 1)
            if tmp * 2 not in visited and 0 <= tmp * 2 <= 100000:
                position_list.append(tmp * 2)
        visited.update(position_list)
        cnt += 1
else:
    cnt += N - K

print(cnt)
