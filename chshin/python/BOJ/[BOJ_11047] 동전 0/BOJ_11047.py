import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

cnt = 0
for coin in coin_list[::-1]:
    if K // coin != 0:
        cnt += K // coin
        K %= coin
    if K == 0:
        break
print(cnt)
