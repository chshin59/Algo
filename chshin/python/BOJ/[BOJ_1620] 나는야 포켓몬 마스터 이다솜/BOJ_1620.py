import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().strip().split())
book1 = {}
book2 = {}
for i in range(1, N+1):
    tmp = sys.stdin.readline().strip()
    book1[hash(i)] = tmp
    book2[tmp] = i


for _ in range(M):
    tmp = sys.stdin.readline().strip()
    if tmp.isdigit():
        print(book1[int(tmp)])
    else:
        print(book2[tmp])
