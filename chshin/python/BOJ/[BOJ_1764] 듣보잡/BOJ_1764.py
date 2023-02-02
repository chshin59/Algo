import sys
input = sys.stdin.readline

N, M = map(int, input().split())

names = dict()
for _ in range(N):
    names[input().rstrip()] = 1

cnt = 0
answers = []

for _ in range(M):
    tmp = input().rstrip()
    if tmp in names:
        cnt += 1
        answers.append(tmp)

answers.sort()
print(cnt)
for answer in answers:
    print(answer)
