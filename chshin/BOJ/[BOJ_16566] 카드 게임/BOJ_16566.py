from bisect import bisect_left
import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
visited = [0] * M

arr1.sort()
for num in arr2:
    idx = bisect_left(arr1, num + 1)
    while visited[idx]:
        idx += 1
    visited[idx] = 1
    print(arr1[idx])
