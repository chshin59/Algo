from collections import deque

rows, columns, queries = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# rows, columns, queries = 3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# rows, columns, queries = 100, 97, [[1,1,100,97]]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def solution(rows, columns, queries):
    matrix = [[0] * columns for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = (r * columns + (c + 1))

    answer = []
    for q in queries:
        dq = deque()
        r1, c1, r2, c2 = map(lambda x: x - 1, q)
        r, c = r1, c1
        r_dif, c_dif = r2 - r1, c2 - c1
        for d in range(4):
            for _ in range([c_dif, r_dif][d % 2]):
                dq.append(matrix[r][c])
                r, c = r + drs[d], c + dcs[d]

        answer.append(min(dq))

        for d in range(4):
            for _ in range([c_dif, r_dif][d % 2]):
                r, c = r + drs[d], c + dcs[d]
                matrix[r][c] = dq.popleft()

    return answer


print(solution(rows, columns, queries))