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

print(len(stack))
