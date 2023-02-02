T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # mCn
    answer = 1
    for m in range(M, M - N, -1):
        answer *= m
    for n in range(1, N + 1):
        answer //= n
    print(answer)
    