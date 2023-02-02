def str_to_seconds(string):
    h, m, s = map(int, string.split(':'))
    return 3600 * h + 60 * m + s


def solution(play_time, adv_time, logs):
    last = str_to_seconds(play_time) + 1
    playbar = [0] * last
    for log in logs:
        s, e = map(str_to_seconds, log.split('-'))
        playbar[s] += 1
        playbar[e] -= 1

    for i in range(1, len(playbar)):
        playbar[i] += playbar[i - 1]
    playbar = playbar[:-1]
    # print(playbar)

    for i in range(1, len(playbar)):
        playbar[i] += playbar[i - 1]
    playbar = [0] + playbar

    # print(playbar)
    answer = total = 0
    advtime = str_to_seconds(adv_time)
    for i in range(len(playbar) - advtime):
        # print(i, i + advtime, playbar[i + advtime] - playbar[i])
        ssum = playbar[i + advtime] - playbar[i]
        if ssum > total:
            total = ssum
            answer = i

    second = answer % 60
    answer //= 60
    minute = answer % 60
    hour = answer // 60

    second = str(second) if second >= 10 else '0' + str(second)
    minute = str(minute) if minute >= 10 else '0' + str(minute)
    hour = str(hour) if hour >= 10 else '0' + str(hour)
    return hour + ':' + minute + ':' + second


print(solution("00:00:10", "00:00:05",["00:00:00-00:00:03", "00:00:02-00:00:05", "00:00:05-00:00:09", "00:00:07-00:00:10"]))
# "00:00:04"
# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# "01:30:59"
# print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# "01:00:00"
# print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
# "00:00:00"
