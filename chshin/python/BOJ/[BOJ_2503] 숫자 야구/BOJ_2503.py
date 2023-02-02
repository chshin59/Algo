from itertools import permutations
import sys
sys.stdin = open('input.txt')

N = int(input())
questions = []
for _ in range(N):
    a, b, c = map(int, input().split())
    questions.append([[a//100, (a // 10) % 10, a % 10], b, c])

cnt = 0
for per in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3):
    p, q, r = per[0], per[1], per[2]
    for question in questions:
        strike = (int(question[0][0] == p) + int(question[0][1] == q) + int(question[0][2] == r))
        ball = (int(p in question[0]) + int(q in question[0]) + int(r in question[0])) - strike
        if strike != question[1] or ball != question[2]:
            break
    else:
        cnt += 1

print(cnt)