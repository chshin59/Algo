import sys
sys.stdin = open('input.txt')


n = int(input())
arr = list(map(int, input().split()))

i, j = 0, n - 1
ssum = float('Inf')
for _ in range(n - 1):
    tmp = arr[i] + arr[j]
    if abs(tmp) < ssum:
        answer = [arr[i], arr[j]]
        ssum = abs(tmp)
    
    if tmp > 0:
        j -= 1
    elif tmp < 0:
        i += 1
    else:
        answer = [arr[i], arr[j]]
        break

print(answer[0], answer[1])