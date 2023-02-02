s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"


def solution(s):
    arr = s.split('},{')

    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[i].split(','))

    arr2[0][0] = arr2[0][0][2:]
    arr2[-1][-1] = arr2[-1][-1][:-2]

    for i in range(len(arr2)):
        if len(arr2[i]) == len(arr2):
            keys = arr2[i]
            break

    d = dict()
    for key in keys:
        d[key] = 0

    for i in range(len(arr2)):
        for j in arr2[i]:
            d[j] += 1

    ans_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for i, j in ans_list:
        answer.append(int(i))

    return answer


print(solution(s))
