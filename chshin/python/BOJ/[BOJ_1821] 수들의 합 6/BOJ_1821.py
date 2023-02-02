import sys
sys.stdin = open('input.txt')


def func(idx, arr2):
    global answer
    if answer:
        return

    if idx == N:
        tmp = 0
        for i in range(N):
            tmp += arr1[i] * arr2[i]
        if tmp == F:
            answer = arr2
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = 1
            func(idx + 1, arr2 + [i])
            visited[i] = 0


N, F = map(int, input().split())

arr1 = [1] * (N)
for i in range((N - 1) // 2 + 1):
    for j in range(1, i + 1):
        arr1[i] *= (N - j)
        arr1[i] //= j
    arr1[N - 1 - i] = arr1[i]

print(arr1)

visited = [0] * (N + 1)
answer = []
func(0, [])
print(*answer)