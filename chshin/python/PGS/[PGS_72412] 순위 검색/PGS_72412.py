def comb(data):
    global d
    d1 = {'cpp': '1', 'java': '2', 'python': '3'}
    d2 = {'backend': '1', 'frontend': '2'}
    d3 = {'junior': '1', 'senior': '2'}
    d4 = {'chicken': '1', 'pizza': '2'}
    for i in ['0', d1[data[0]]]:
        for j in ['0', d2[data[1]]]:
            for k in ['0', d3[data[2]]]:
                for l in ['0', d4[data[3]]]:
                    d[i + j + k + l].append(data[-1])


def query_to_key(conditions):
    key = ''
    for condition in conditions:
        if condition == '-':
            key += '0'
        elif condition in ['cpp', 'backend', 'junior', 'chicken']:
            key += '1'
        elif condition in ['java', 'frontend', 'senior', 'pizza']:
            key += '2'
        elif condition == 'python':
            key += '3'
    return key


def over_score(lst, target):
    n = len(lst)
    l, r = 0, n - 1
    c = (l + r) // 2
    while l < r:
        if lst[c] < target:
            l = c + 1
        elif lst[c] >= target:
            r = c
        c = (l + r) // 2
    if c == n - 1:
        if lst[-1] < target:
            return 0
    return n - c


def solution(info, query):
    global d

    d = dict()
    # 딕셔너리에 키만 먼저 만들어 줌
    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    d[str(i) + str(j) + str(k) + str(l)] = []

    # 딕셔너리 채우기
    for data in info:
        data = data.split()
        data[-1] = int(data[-1])
        comb(data)

    # 이진 탐색을 위해 미리 정렬
    for key, value in d.items():
        d[key] = sorted(value)

    answer = []
    for q in query:
        q = q.split()
        q, score = q[::2], int(q[-1])

        key = query_to_key(q)

        values = d[key]
        answer.append(over_score(values, score)) if values else answer.append(0)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))

# print(over_score([1, 2, 3, 4, 5, 6, 8, 9, 10], 11))