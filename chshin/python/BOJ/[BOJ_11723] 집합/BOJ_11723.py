import sys

sys.stdin = open('input.txt')

M = int(input())

set_num = 1
for _ in range(M):
    func = sys.stdin.readline().rstrip()
    if ' ' in func:
        func, x = func.split()
        x = int(x)
        if func == 'add':
            set_num = set_num | 2 ** x
        elif func == 'remove':
            set_num = set_num & ~(2 ** x)
        elif func == 'check':
            print(int(bool(set_num & 2 ** x)))
        elif func == 'toggle':
            set_num = set_num ^ 2 ** x
    else:
        if func == 'all':
            set_num = 0b111111111111111111111
        elif func == 'empty':
            set_num = 1
