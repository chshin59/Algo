import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
arr2 = [0] * (N + 1)
for i in range(2, N + 1):
    arr2[i] = arr2[i - 1] + 1 if arr[i] < arr[i - 1] else arr2[i - 1]

Q = int(input())
for _ in range(Q):
    s, e = map(int, input().split())
    print(arr2[e] - arr2[s])
