import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
xx = []
yy = []
for _ in range(n):
    x, y = map(int, input().split())
    xx.append(x)
    yy.append(y)
xx.append(xx[0])
yy.append(yy[0])

print(xx)
print(yy)

S = 0
for i in range(n):
    S += xx[i] * yy[i+1] - xx[i+1] * yy[i]
S = 0.5 * abs(S)
print(f'{S:.1f}')
