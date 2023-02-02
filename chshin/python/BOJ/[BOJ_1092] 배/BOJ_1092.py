import sys
sys.stdin = open('input.txt')

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        if cranes[i] > cranes[j]:
            cranes[i], cranes[j] = cranes[j], cranes[i]

cnt_list = []
for i in range(N):
    cnt = 0
    j = 0
    while j < len(boxes):
        if boxes[j] <= cranes[i]:
            cnt += 1
            del boxes[j]
        else:
            j += 1
    cnt_list.append(cnt)

ssum = 0
for cnt in cnt_list:
    ssum += cnt

if ssum < M:
    print(-1)
else:
    answer = 0
    k = N - 1
    ssum = 0
    while k >= 0:
        ssum += cnt_list[k]
        tmp = ssum / (N-k)
        tmp = int(tmp) + 1 if tmp - int(tmp) > 0 else int(tmp)
        if tmp > answer:
            answer = tmp
        k -= 1

    print(answer)
