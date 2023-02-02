def func(lst, answer, cnt):
    if not cnt:
        print(' '.join(map(str, answer)))
        return
    if not lst:
        return

    # 선택
    func(lst[1:], answer + [lst[0]], cnt - 1)

    # 선택x
    func(lst[1:], answer, cnt)


N, M = map(int, input().split())
lst = list(range(1, N+1))
func(lst, [], M)
