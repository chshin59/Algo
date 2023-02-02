import sys
sys.stdin = open('input.txt')


def func(l, r):
    global answer
    if r < l:
        return

    tmp = arr[l]
    for i in range(l+1, r+1):
        if arr[i][1] < tmp[1]:
            tmp = arr[i]

    answer.append(tmp)
    answer.sort()
    print(''.join(map(lambda x: x[1], answer)))

    idx = tmp[0]
    func(idx + 1, r)
    func(l, idx - 1)


word = input()
n = len(word)
l, r, answer = 0, n - 1, []
arr = [(i, word[i]) for i in range(n)]
func(l, r)
