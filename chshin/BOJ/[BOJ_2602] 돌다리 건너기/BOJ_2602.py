import sys
sys.stdin = open('input.txt')


def func(position):
    new_answer1 = answer1[:]
    new_answer2 = answer2[:]
    for idx in range(N):
        if scroll[idx] == bridge1[position]:
            if idx == 0:
                new_answer1[0] += 1
            else:
                new_answer1[idx] += answer2[idx - 1]
    for idx in range(N):
        if scroll[idx] == bridge2[position]:
            if idx == 0:
                new_answer2[0] += 1
            else:
                new_answer2[idx] += answer1[idx - 1]
    return new_answer1, new_answer2


scroll = list(input())
bridge1 = list(input())
bridge2 = list(input())
N = len(scroll)
answer1 = [0 for _ in range(N)]
answer2 = [0 for _ in range(N)]

if bridge1[0] == scroll[0]:
    answer1[0] += 1
if bridge2[0] == scroll[0]:
    answer2[0] += 1

for position in range(1, len(bridge1)):
    answer1, answer2 = func(position)
print(answer1[-1] + answer2[-1])
