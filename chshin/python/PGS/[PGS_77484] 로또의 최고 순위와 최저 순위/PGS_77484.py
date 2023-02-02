lottos, win_nums = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
# lottos, win_nums = [0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]
# lottos, win_nums = [45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]


def solution(lottos, win_nums):
    match_cnt = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto and lotto in win_nums:
            match_cnt += 1
        elif not lotto:
            zero_cnt += 1

    answer = []
    for num in [match_cnt + zero_cnt, match_cnt]:
        if num >= 2:
            answer.append(7 - num)
        else:
            answer.append(6)

    return answer


print(solution(lottos, win_nums))