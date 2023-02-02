"""
f(1) = 1
f(2) = 3
f(3) = f(2) + f(1) * 2

f(n+2) = f(n+1) + 2f(n)

f(n+2) + f(n+1) = 2(..)
f(n+2) - 2f(n+1) = -(..)

f(n+1) + f(n) = (2 ** n-1) * 4
f(n+1) - 2f(n) = ((-1) ** n-1) * 1
3f(n) = 2 ** (n+1) + (-1) ** n

f(n) = (2 ** (n + 1) + (-1) ** n)/3

"""

n = int(input())
arr = [0, 1, 3]
if n < 3:
    print(arr[n])
else:
    for i in range(3, n + 1):
        arr.append(arr[i - 1] + 2 * arr[i - 2])
    print(arr[n] % 10007)

# print((2 ** (n + 1) + (-1) ** n) // 3 % 10007)
