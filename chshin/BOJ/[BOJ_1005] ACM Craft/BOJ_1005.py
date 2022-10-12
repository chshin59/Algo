import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    bd_times = [0] + list(map(int, input().split()))

    tree = [[] for _ in range(N+1)]
    in_degree = [0] * (N + 1)
    for _ in range(K):
        i, j = map(int, input().split())
        tree[i].append(j)
        in_degree[j] += 1

    lst_bd = int(input())
    dq = deque()
    for i in range(1, N + 1):
        if not in_degree[i]:
            dq.append(i)

    answer = bd_times[:]
    while dq:
        prev_bd = dq.popleft()
        if not in_degree[lst_bd]:
            break
        for next_bd in tree[prev_bd]:
            in_degree[next_bd] -= 1
            answer[next_bd] = max(answer[next_bd], answer[prev_bd] + bd_times[next_bd])
            if not in_degree[next_bd]:
                dq.append(next_bd)

    print(answer[lst_bd])
