from itertools import combinations


def solution(orders, course):
    n = len(orders)
    d = dict()
    # 1
    for idx in range(n):
        for c in course:
            for tmp in combinations(sorted(orders[idx]), c):
                tmp = ''.join(tmp)
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 1
    print(d)

    # 2
    d2 = {c: [] for c in course}
    for k, v in d.items():
        if v > 1:
            d2[len(k)].append([k, v])
    print(d2)

    # 3
    answer = []
    for k, v in d2.items():
        if v:
            v.sort(key=lambda x: -x[1])
            tmp = v[0][-1]
            for a in v:
                if a[-1] == tmp:
                    answer.append(a[0])
                else:
                    break
    print(answer)

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# ["AC", "ACDE", "BCFG", "CDE"]
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
# ["WX", "XY"]
