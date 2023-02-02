import sys
sys.stdin = open('input.txt')


def add1(r, c, a, tmp):
    used_nums_r[r].add(tmp)
    used_nums_c[c].add(tmp)
    used_nums_a[a].add(tmp)


def remove1(r, c, a, tmp):
    used_nums_r[r].remove(tmp)
    used_nums_c[c].remove(tmp)
    used_nums_a[a].remove(tmp)


def dfs(num):
    if num == 81:
        return 1

    r, c = num // 9, num % 9
    if matrix[r][c]:
        return dfs(num + 1)
    else:
        a = (r // 3) * 3 + (c // 3)
        candidate = set(range(1, 10)) - used_nums_r[r] - used_nums_c[c] - used_nums_a[a]
        for tmp in sorted(candidate):
            add1(r, c, a, tmp)
            matrix[r][c] = tmp
            if dfs(num + 1):
                return 1
            matrix[r][c] = 0
            remove1(r, c, a, tmp)


matrix = [list(map(int, list(input()))) for _ in range(9)]

used_nums_r = [set() for _ in range(9)]
used_nums_c = [set() for _ in range(9)]
used_nums_a = [set() for _ in range(9)]

for r in range(9):
    for c in range(9):
        if matrix[r][c]:
            add1(r, c, (r // 3) * 3 + (c // 3), matrix[r][c])

dfs(0)
for row in matrix:
    print(*row, sep='')