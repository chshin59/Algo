import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def func1(x):
    return str(dict1[x])


N = int(input())
lst = list(map(int, input().rstrip().split()))

tmp = sorted(list(set(lst)))

dict1 = dict()
for i, j in enumerate(tmp):
    dict1[j] = i

print(' '.join(list(map(func1, lst))))
