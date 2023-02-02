import sys
sys.stdin = open('input.txt')

for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    # 1
    if x3 < x1 and y3 < y1:
        if x4 == x1 and y4 == y1:
            print('c')
        elif x4 < x1 or y4 < y1:
            print('d')
        elif (x4 == x1 and y4 > y1) or (y4 == y1 and x4 > x1):
            print('b')
        else:
            print('a')
    # 2, 3
    if x1 <= x3 < x2 and y3 < y1:
        if y4 < y1:
            print('d')
        elif y4 == y1:
            print('b')
        else:
            print('a')
    # 6, 11
    if y1 <= y3 < y2 and x3 < x1:
        if x4 < x1:
            print('d')
        elif x4 == x1:
            print('b')
        else:
            print('a')
    # 4
    if x3 == x2 and y3 < y1:
        if y4 < y1:
            print('d')
        elif y4 == y1:
            print('c')
        else:
            print('b')
    # 16
    if y3 == y2 and x3 < x1:
        if x4 < x1:
            print('d')
        elif x4 == x1:
            print('c')
        else:
            print('b')
    # 7, 8, 12, 13
    if x1 <= x3 < x2 and y1 <= y3 < y2:
        print('a')
    # 9, 14
    if x3 == x2 and y1 <= y3 < y2:
        print('b')
    # 17, 18
    if y3 == y2 and x1 <= x3 < x2:
        print('b')
    # 19
    if x3 ==x2 and y3 == y2:
        print('c')
    # 5, 10, 15, 20, 21, 22, 23, 24, 25
    if x3 > x2 or y3 > y2:
        print('d')
