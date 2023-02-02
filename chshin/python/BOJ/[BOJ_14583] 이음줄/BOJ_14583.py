import sys
sys.stdin = open('input.txt')

from math import cos, tan, atan

H, V = map(float, input().split())
theta = 0.5 * atan(V/H)
height = (V - H * tan(theta)) * cos(theta)
width = 0.5 * H / cos(theta)
print(f'{width:.2f} {height:.2f}')
