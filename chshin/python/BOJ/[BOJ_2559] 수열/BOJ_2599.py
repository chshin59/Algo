import sys
sys.stdin = open('input1.txt')

N, K = map(int, input().split())
temps = list(map(int, input().split()))
tmp_sum = sum(temps[0:K])
answer = tmp_sum

for i in range(N-K):
    tmp_sum += (temps[i+K] - temps[i])
    if answer < tmp_sum:
        answer = tmp_sum
print(answer)
