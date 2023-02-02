def func(arr, d, cnt):
    if cnt == n:
        print(''.join(arr))
        return

    keys = []
    for key, value in d.items():
        if value != 0:
            keys.append(key)

    for tmp in keys:
        d[tmp] -= 1
        func(arr + [tmp], d, cnt + 1)
        d[tmp] += 1


N = int(input())
for _ in range(N):
    word = list(input())
    n = len(word)

    strings = dict()
    for i in sorted(set(word)):
        strings[i] = word.count(i)

    func([], strings, 0)
