import sys
sys.stdin = open('input.txt')

string = input()
n = len(string)
idx = cnt = 0
flag = 1

while idx < n:
    if string[idx] == 'w':
        cnt += 1
        idx += 1
    elif cnt == 0:
        print(0)
        flag = 0
        break
    else:
        tmp = 'o' * cnt + 'l' * cnt + 'f' * cnt
        if string[idx:idx + 3 * cnt] != tmp:
            print(0)
            flag = 0
            break
        idx += 3 * cnt
        cnt = 0
if flag:
    print(0) if cnt else print(1)
