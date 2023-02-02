import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

i = j = 0
answer = N + 1
ssum = numbers[0]
while j != N - 1 or ssum >= S:
    if ssum < S:
        j += 1
        ssum += numbers[j]
    else:
        if j - i + 1 < answer:
            answer = j - i + 1
        ssum -= numbers[i]
        i += 1

if answer == N + 1:
    print(0)
else:
    print(answer)
