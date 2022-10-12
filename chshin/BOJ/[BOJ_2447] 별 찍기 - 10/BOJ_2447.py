def func(i, j, N):
    if N == 1:
        return
    N //= 3
    for r in range(3):
        for c in range(3):
            if (r, c) == (1, 1):
                for p in range(i + N, i + 2 * N):
                    for q in range(j + N, j + 2 * N):
                        matrix[p][q] = ' '
            else:
                func(i + r * N, j + c * N, N)


N = int(input())
matrix = [['*'] * N for _ in range(N)]
func(0, 0, N)
for r in range(N):
    print(*matrix[r], sep='')