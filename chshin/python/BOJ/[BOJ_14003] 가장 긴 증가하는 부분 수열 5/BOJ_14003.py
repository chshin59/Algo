from bisect import bisect_left
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
idxs = [0] * N

stack = [arr[0]]
for i in range(1, N):
    num = arr[i]
    if num > stack[-1]:
        stack.append(arr[i])
        idxs[i] = len(stack) - 1
    else:
        tmp = bisect_left(stack, num)
        idxs[i] = tmp
        stack[tmp] = num

answer = []
n = len(stack)
for i in range(N - 1, -1, -1):
    if idxs[i] == n - 1:
        answer.append(arr[i])
        n -= 1

print(len(stack))
print(*reversed(answer))
