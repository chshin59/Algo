N = int(input())
arr = list(map(int, input().split()))

asc = [1] * N
desc = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            asc[i] = max(asc[i], asc[j] + 1)

for i in range(N - 2, -1, -1):
    for j in range(N - 1, i, -1):
        if arr[j] < arr[i]:
            desc[i] = max(desc[i], desc[j] + 1)

answer = 0
for i in range(N):
    answer = max(answer, asc[i] + desc[i] - 1)
print(answer)