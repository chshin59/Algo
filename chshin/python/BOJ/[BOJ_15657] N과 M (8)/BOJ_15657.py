def func(lst, answer, cnt):
    if not cnt:
        print(' '.join(map(str, answer)))
        return
    if not lst:
        return

    for i in range(len(lst)):
        func(lst[i:], answer + [lst[i]], cnt - 1)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
func(lst, [], M)
