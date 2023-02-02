import heapq

N = int(input())
hw = {day: [] for day in range(1, 1001)}
last_day = 0
for _ in range(N):
    d, w = map(int, input().split())
    if d > last_day:
        last_day = d
    hw[d].append(-w)

answer = 0
scores = []
for day in range(last_day, 0, -1):
    scores.extend(hw[day])
    heapq.heapify(scores)
    if scores:
        answer += heapq.heappop(scores)
print(-answer)
