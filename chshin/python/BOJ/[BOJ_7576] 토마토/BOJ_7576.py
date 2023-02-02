import sys
sys.stdin = open('input.txt')


def BFS(matrix, start):
    queue = start
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    answer = -1

    while queue:
        tmp = []
        for q in queue:
            for d in range(4):
                new_x = q[0] + dxs[d]
                new_y = q[1] + dys[d]
                if 0 <= new_x < N and 0 <= new_y < M and matrix[new_x][new_y] == 0:
                    tmp.append([new_x, new_y])
                    matrix[new_x][new_y] = 1
        queue = tmp
        answer += 1

    for i in range(N):
        if 0 in matrix[i]:
            return -1
    return answer    


M, N = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

start = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            start.append([i, j])

print(BFS(matrix, start))
