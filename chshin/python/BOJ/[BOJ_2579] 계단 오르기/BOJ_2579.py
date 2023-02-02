N = int(input())
arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())

"""
f(0) = 0
f(1) = A1
f(2) = A1 + A2
점화식
f(n) = max(f(n-2), f(n-3) + An-1) + An
"""
if N < 3:
    print(sum(arr))
else:
    arr2 = [0] * (N + 1)
    arr2[1], arr2[2] = arr[1], arr[1] + arr[2]
    for i in range(3, N + 1):
        arr2[i] = max(arr2[i-2], arr2[i-3] + arr[i-1]) + arr[i]
    print(arr2[-1])
