# stack 만들기
# [6]
# [9]
# [9, 5]
# [9, 7]
# [9, 7, 4]


import sys
sys.stdin = open('input.txt')

# 스택 활용
N = int(input())
towers = [100000001] + list(map(int, input().split()))

stack_i = [0]
answer = []

for i in range(1, N+1):
    while towers[i] > towers[stack_i[-1]]:
        stack_i.pop()
    answer.append(stack_i[-1])
    stack_i.append(i)

print(' '.join(map(str, answer)))


# 시간복잡도 n2
# N = int(input())
# towers = list(map(int, input().split()))
#
# answer = [0] * N
#
# for i in range(N):
#     for j in range(i+1, N):
#         if towers[i] >= towers[j]:
#             answer[j] = i + 1
#         else:
#             break
#
# print(' '.join(map(str, answer)))
