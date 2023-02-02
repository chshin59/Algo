import sys
sys.stdin = open('input.txt')


def func(answer, idx,  vowel_cnt):
    if len(answer) == L:
        if vowel_cnt >= 1 and L - vowel_cnt >= 2:
            print(''.join(answer))
        return

    if idx >= C:
        return

    for c in range(idx, C):
        if not selected[c]:
            selected[c] = 1
            if arr[c] in vowels:
                func(answer + [arr[c]], c + 1, vowel_cnt + 1)
            else:
                func(answer + [arr[c]], c + 1, vowel_cnt)
            selected[c] = 0


L, C = map(int, input().split())
arr = input().split()
arr.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
selected = [0] * C

func([], 0, 0)