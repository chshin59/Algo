import heapq
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
left = []
right = []
center = int(input())
print(center)

if N >= 2:
    tmp = int(input())
    if tmp >= center:
        heapq.heappush(right, tmp)
    else:
        heapq.heappush(right, center)
        center = tmp
    print(center)

for i in range(N - 2):
    tmp = int(input())
    if i % 2:
        if tmp >= center:
            heapq.heappush(right, tmp)
        elif -left[0] <= tmp < center:
            heapq.heappush(right, center)
            center = tmp
        else:
            heapq.heappush(right, center)
            center = -heapq.heappop(left)
            heapq.heappush(left, -tmp)
    else:
        if tmp <= center:
            heapq.heappush(left, -tmp)
        elif center < tmp <= right[0]:
            heapq.heappush(left, -center)
            center = tmp
        else:
            heapq.heappush(left, -center)
            center = heapq.heappop(right)
            heapq.heappush(right, tmp)
    print(center)
