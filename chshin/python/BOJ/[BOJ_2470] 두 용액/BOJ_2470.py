import sys
sys.stdin = open('input.txt')


def func(i, j):
    global answer, ssum
    tmp = ssum
    while i < j:
        if tmp == 0:
            print(lst[i], lst[j])
            return
        if abs(tmp) < abs(ssum):
            answer = i, j
            ssum = tmp

        if tmp > 0:
            tmp -= lst[j]
            j -= 1
            tmp += lst[j]
        elif tmp < 0:
            tmp -= lst[i]
            i += 1
            tmp += lst[i]
    print(lst[answer[0]], lst[answer[1]])


N = int(input())
lst = list(map(int, input().split()))
lst.sort()

if lst[0] >= 0:
    print(lst[0], lst[1])

elif lst[-1] <= 0:
    print(lst[-2], lst[-1])

else:
    i, j = 0, N - 1
    ssum = lst[i] + lst[j]
    answer = i, j
    func(i, j)
