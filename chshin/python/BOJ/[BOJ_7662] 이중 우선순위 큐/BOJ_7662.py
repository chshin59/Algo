import heapq
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    d = dict()
    heap1 = []
    heap2 = []
    for _ in range(k):
        oper, num = input().split()
        num = int(num)
        if oper == "I":
            d.setdefault(num, 0)
            d[num] += 1
            heapq.heappush(heap1, num)
            heapq.heappush(heap2, -num)
        else:
            if num == 1:
                while True:
                    if not heap2:
                        break
                    tmp = -heapq.heappop(heap2)
                    if d[tmp]:
                        d[tmp] -= 1
                        break
            else:
                while True:
                    if not heap1:
                        break
                    tmp = heapq.heappop(heap1)
                    if d[tmp]:
                        d[tmp] -= 1
                        break
    answer = []
    for k, v in d.items():
        if v:
            answer.append(k)
    answer.sort()
    print(answer[-1], answer[0]) if answer else print('EMPTY')

