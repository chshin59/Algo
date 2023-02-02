import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]


max_score = -float('inf')

for n in range(1, N+1):
    arr_n = [0] * (M+1)
    for i in range(n, N+1):
        tmp = [0] * (M+1)
        for j in range(1, M+1):
            arr_n[j] += arr[i][j]
            tmp[j] = max(arr_n[j], tmp[j-1]+arr_n[j])
            max_score = max(tmp[j], max_score)

print(max_score)
