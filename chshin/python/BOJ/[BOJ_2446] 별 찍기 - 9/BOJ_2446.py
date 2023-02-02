N = int(input())

i = 0
for _ in range(2*N-1):
    print(" " * (i), end="")
    print("*" * (2*N - 2*i - 1))
    if _ < N-1:
        i += 1
    else:
        i -= 1