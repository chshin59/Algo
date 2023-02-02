import sys

sys.stdin = open('input.txt')


def dfs(virus):
    lab[virus[0]][virus[1]] = 2
    for i in range(4):
        x = virus[0] + dxs[i]
        y = virus[1] + dys[i]
        if 0 <= x < N and 0 <= y < M and not lab[x][y]:
            dfs([x, y])


N, M = map(int, input().split())
lab_tmp = []
for _ in range(N):
    lab_tmp.extend(list(map(int, input().split())))

viruses = []
for i in range(len(lab_tmp)):
    if lab_tmp[i] == 2:
        viruses.append([i // M, i % M])

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

answer = 0
for p in range(N * M):
    for q in range(p + 1, N * M):
        for r in range(q + 1, N * M):
            if not lab_tmp[p] and not lab_tmp[q] and not lab_tmp[r]:
                lab = lab_tmp[:]
                lab[p], lab[q], lab[r] = 1, 1, 1
                lab = [lab[s * M: (s+1) * M] for s in range(N)]

                for virus in viruses:
                    dfs(virus)

                tmp = 0
                for i in range(N):
                    tmp += lab[i].count(0)
                if tmp > answer:
                    answer = tmp
print(answer)
