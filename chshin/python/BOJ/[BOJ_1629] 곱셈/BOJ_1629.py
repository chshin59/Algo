def func(power):
    if power == 1:
        return D

    if power % 2:
        return ((func(power // 2) ** 2) * D) % C
    else:
        return (func(power // 2) ** 2) % C


A, B, C = map(int, input().split())
D = A % C
print(func(B))
