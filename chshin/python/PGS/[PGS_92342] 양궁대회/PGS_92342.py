def solution(n, info):
    global answer, answer_total
    answer = [0] * 11
    answer_total = 0

    lst = [0] * 11

    def func(idx, cnt, lst):
        global answer, answer_total

        if cnt < 0:
            return

        if idx == 10:
            lst[idx] = cnt
            ssum = 0
            for i in range(10):
                if lst[i]:
                    ssum += 10 - i
                else:
                    if info[i]:
                        ssum -= 10 - i

            if ssum > answer_total:
                answer = lst[:]
                answer_total = ssum
            elif ssum == answer_total:
                for i in range(10, -1, -1):
                    if lst[i] > answer[i]:
                        answer = lst[:]
                        answer_total = ssum
                        break
                    elif lst[i] < answer[i]:
                        break
            return

        lst[idx] = info[idx] + 1
        func(idx + 1, cnt - lst[idx], lst)

        lst[idx] = 0
        func(idx + 1, cnt, lst)

    func(0, n, lst)
    if answer_total == 0:
        answer = [-1]
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
