import sys
sys.stdin = open('input.txt')


def explode(stack):
    if len(stack) < M:
        return

    for i in range(-1, -M - 1, -1):
        if stack[i] != str2[i]:
            return

    for _ in range(M):
        stack.pop()


str1 = list(input())
str2 = list(input())
N, M = len(str1), len(str2)

stack = []
for i in range(N):
    stack.append(str1[i])
    explode(stack)
print(''.join(stack)) if stack else print('FRULA')
