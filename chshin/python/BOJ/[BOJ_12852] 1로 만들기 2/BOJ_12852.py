from collections import deque


def find(N):
    answer.append(N)
    if parents[N] == N:
        return
    find(parents[N])


N = int(input())
parents = [0] * (N + 1)
parents[1] = 1
counts = [0] * (N + 1)

dq = deque([[1, 0]])
while not parents[N]:
    num, cnt = dq.popleft()
    for num2 in [num + 1, 2 * num, 3 * num]:
        if num2 == N:
            parents[num2] = num
            counts[num2] = cnt + 1
            break
        elif num2 <= N and not counts[num2]:
            dq.append([num2, cnt + 1])
            parents[num2] = num
            counts[num2] = cnt + 1

answer = []
find(N)
print(counts[N])
print(*answer)