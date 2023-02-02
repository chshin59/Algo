import sys
sys.stdin = open('input.txt')

N = int(input())
people = list(map(int, input().split()))
people.sort()

answer = 0
for i in range(N):
    answer += people[i] * (N-i)

# tmp = 0
# answer = 0
# for x in people:
#     tmp += x
#     answer += tmp

print(answer)
