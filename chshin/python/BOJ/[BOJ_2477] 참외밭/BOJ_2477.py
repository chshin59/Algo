import sys

sys.stdin = open('input.txt')


def my_max(lst):
    value = lst[0]
    for i in lst[1:]:
        if i > value:
            value = i
    return value


K = int(input())
m = []
n = []
for i in range(6):
    n.append(int(input()[2:])) if i % 2 else m.append(int(input()[2:]))

l_square = my_max(m) * my_max(n)

for i in range(3):
    if m[i] == my_max(m):
        m_index = i
for j in range(3):
    if n[j] == my_max(n):
        n_index = j

if m_index == n_index:
    s_square = n[(n_index + 1) % 3] * m[(m_index + 2) % 3]
else:
    s_square = m[(m_index + 1) % 3] * n[(n_index + 2) % 3]

print((l_square - s_square) * K)
