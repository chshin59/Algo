import sys
sys.stdin = open('input.txt')

FC, VC, P = map(int, input().split())
BE = int(FC / (P - VC) + 1) if P > VC else -1
print(BE)
