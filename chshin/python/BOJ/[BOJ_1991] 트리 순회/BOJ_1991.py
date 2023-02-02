import sys
sys.stdin = open('input.txt')


def traversal(num):
    l = left_child[num]
    r = right_child[num]

    answer[0].append(chr(num+64))
    if l:
        traversal(l)

    answer[1].append(chr(num+64))
    if r:
        traversal(r)
    answer[2].append(chr(num+64))


N = int(input())
left_child = [0] * (N + 1)
right_child = [0] * (N + 1)
for _ in range(1, N + 1):
    p, lc, rc = input().split()
    if lc != '.':
        left_child[ord(p)-64] = ord(lc) - 64
    if rc != '.':
        right_child[ord(p)-64] = ord(rc) - 64

answer = [[], [], []]
traversal(1)
for i in range(3):
    print(''.join(answer[i]))
