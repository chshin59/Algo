import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]

for r in range(X, H):
    for c in range(Y, W):
        B[r][c] -= B[r-X][c-Y]
A = [B[h][:W] for h in range(H)]
for h in range(H):
    print(*A[h])
