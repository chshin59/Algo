def func(selected, nexts, sheep, wolf, info):
    global answer, c1, c2
    # 종료조건
    if sheep == wolf:
        return
    print(selected)
    if sheep > answer:
        answer = sheep

    for idx in range(len(nexts)):
        x = nexts[idx]
        new_selected = selected + [x]
        new_wolf, new_sheep = wolf, sheep
        if info[x]:
            new_wolf += 1
        else:
            new_sheep += 1
        new_nexts = nexts[:idx] + nexts[idx + 1:]
        if c1[x] != -1:
            if c2[x] != -1:
                new_nexts.extend([c1[x], c2[x]])
            else:
                new_nexts.extend([c1[x]])
        func(new_selected, new_nexts, new_sheep, new_wolf, info)


def solution(info, edges):
    global answer, c1, c2
    n = len(info)
    c1 = [-1] * n
    c2 = [-1] * n
    for edge in edges:
        p, c = edge
        if c1[p] == -1:
            c1[p] = c
        else:
            c2[p] = c

    answer = 0
    if c2[0] == -1:
        func([0], [c1[0]], 1, 0, info)
    else:
        func([0], [c1[0], c2[0]], 1, 0, info)
    return answer


# info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
# edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
print(solution(info, edges))
