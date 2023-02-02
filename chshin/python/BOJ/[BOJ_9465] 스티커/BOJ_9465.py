import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst1 = list(map(int, input().split()))

    memo = [[0]*N for _ in range(2)]
    memo[0][0] = lst[0]
    memo[1][0] = lst1[0]

    if N != 1:
        memo[0][1] = lst[1] + lst1[0]
        memo[1][1] = lst1[1] + lst[0]

    for i in range(2, N):
        memo[0][i] = lst[i] + max(memo[1][i-2], memo[1][i-1])
        memo[1][i] = lst1[i] + max(memo[0][i-2], memo[0][i-1])

    print(max(memo[0][N-1], memo[1][N-1]))
