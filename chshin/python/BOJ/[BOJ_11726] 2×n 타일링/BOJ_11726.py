def func(n):
    lst = [1, 2]
    if n == 1:
        return 1
    for i in range(n-2):
        lst.append(lst[-1]+lst[-2])
    return lst[-1]


n = int(input())
print(func(n) % 10007)
