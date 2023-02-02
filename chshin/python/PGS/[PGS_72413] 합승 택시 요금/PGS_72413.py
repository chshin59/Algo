def func(s, e, graph):
    n = len(graph) - 1

    D = dict()
    for i in range(1, n + 1):
        D[i] = float('inf')

    U = set()
    U.add(s)

    D[s] = 0
    for v, price in graph[s]:
        D[v] = price

    while len(U) < n:
        # w 선택
        tmp = float('inf')
        for key in set(D.keys()) - U:
            if D[key] <= tmp:
                w, tmp = key, D[key]

        # e가 선택되면 탐색 종료
        if w == e:
            break

        # U에 추가
        U.add(w)

        # 비용 갱신
        for v, price in graph[w]:
            D[v] = min(D[v], D[w] + price)
    return D[e]


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        p, q, r = fare
        graph[p].append((q, r))
        graph[q].append((p, r))

    # 합승을 안하는 경우
    answer = func(s, a, graph) + func(s, b, graph)

    # 합승을 하는 경우
    # 합승이 끝나는 지점 = v
    for v in set(range(1, n + 1)) - {s}:
        ssum = func(s, v, graph)
        ssum += func(v, a, graph) + func(v, b, graph)
        if ssum < answer:
            answer = ssum
    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
