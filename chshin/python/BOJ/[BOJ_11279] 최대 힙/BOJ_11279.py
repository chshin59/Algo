import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
numbers = []

for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if numbers:
            print(-heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, -x)
