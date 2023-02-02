import sys
sys.stdin = open('input2.txt')

N = int(input())
lst = list(map(int, input().split()))

i = 1
j = 1
cnt = 1
max_cnt = 1
flag = '='
while i < N:
    # 증가
    if lst[i] > lst[i-1]:
        # 감소
        if flag == '-':
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
            flag = '+'
            i = i - j
            j = 1

        # 증가, =
        else:
            j = 1
            cnt += 1
            flag = '+'
    # 감소
    elif lst[i] < lst[i-1]:
        # 증가
        if flag == '+':
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
            flag = '-'
            i = i - j
            j = 1
        # 감소, =
        else:
            j = 1
            cnt += 1
            flag = '-'
    # =
    else:
        cnt += 1
        j += 1

    i += 1

# 마지막으로 대소 비교
if max_cnt < cnt:
    max_cnt = cnt

print(max_cnt)
