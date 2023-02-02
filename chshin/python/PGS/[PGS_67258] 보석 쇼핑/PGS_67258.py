gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]


def solution(gems):
    set1 = set(gems)
    d = dict()
    for gem in set1:
        d[gem] = 0
    n = len(gems)

    answer = [0, n - 1]
    i, j = 0, -1
    set2 = set()
    while j != n - 1 or len(set2) == len(set1):
        print(d, set2)
        if len(set2) != len(set1):
            j += 1
            d[gems[j]] += 1
            set2.add(gems[j])
        else:
            if j - i < answer[1] - answer[0]:
                answer = [i, j]
            d[gems[i]] -= 1
            if d[gems[i]] == 0:
                set2.discard(gems[i])
            i += 1

    answer[0] += 1
    answer[1] += 1
    return answer


print(solution(gems))
