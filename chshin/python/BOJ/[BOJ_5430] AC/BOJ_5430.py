import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    funcs = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    lst = sys.stdin.readline().rstrip()[1:-1].split(',')

    i, j = 0, N
    front = True

    R_cnt = D_cnt = 0
    for func in funcs:
        if func == 'R':
            R_cnt += 1
            front = not front
        else:
            D_cnt += 1
            if front:
                i += 1
            else:
                j -= 1
    if D_cnt > N:
        print('error')
    elif D_cnt == N:
        print('[]')
    else:
        if R_cnt % 2:
            print('[' + ','.join(lst[i:j][::-1]) + ']')
        else:
            print('[' + ','.join(lst[i:j]) + ']')
