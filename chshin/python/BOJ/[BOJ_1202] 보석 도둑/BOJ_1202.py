import heapq
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    heapq.heappush(jewels, list(map(int, input().split())))

bags = [int(input()) for _ in range(K)]
bags.sort()


# 가방을 순서대로 탐색
answer = 0
hq = []
for bag in bags:
    # 보석을 순서대로 탐색하면서
    # 무게가 작으면 hq에 가격을 넣음
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(hq, -heapq.heappop(jewels)[1])
    # hq안에서 가장 높은 가격인 V를 pop
    if hq:
        answer += -heapq.heappop(hq)
print(answer)