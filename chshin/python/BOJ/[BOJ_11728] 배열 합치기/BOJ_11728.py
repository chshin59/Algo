import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []
a_idx = b_idx = 0
for _ in range(N + M):
    if A[a_idx] < B[b_idx]:
        answer.append(A[a_idx])
        a_idx += 1
    else:
        answer.append(B[b_idx])
        b_idx += 1
    if a_idx == N:
        answer.extend(B[b_idx:])
        break
    if b_idx == M:
        answer.extend(A[a_idx:])
        break
print(' '.join(map(str, answer)))
