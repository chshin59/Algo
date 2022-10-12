import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if not arr[0]:
        break
    N = arr[0]
    arr = arr[1:] + [0]
    stack = []
    answer = 0
    for j in range(len(arr)):
        tmp = j
        while stack and stack[-1][0] > arr[j]:
            height, i = stack.pop()
            answer = max(answer, height * (j - i))
            tmp = i
        stack.append((arr[j], tmp))
    print(answer)
