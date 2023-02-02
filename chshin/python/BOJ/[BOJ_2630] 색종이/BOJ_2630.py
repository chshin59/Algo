import sys
sys.stdin = open('input.txt')

def func(lst, N):
    global blue, white
    if sum(map(sum, lst)) == 0:
        white += 1
    elif sum(map(sum, lst)) == N ** 2:
        blue += 1
    else:
        N2 = N // 2
        for i in [0, N2]:
            for j in [0, N2]:
                lst2 = [lst[i+k][j:j+N2] for k in range(0, N2)]
                func(lst2, N2)
                

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

white = blue = 0
func(paper, N)
print(white)
print(blue)
