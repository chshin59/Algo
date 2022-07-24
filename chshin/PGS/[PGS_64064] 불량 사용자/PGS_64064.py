user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]


def check(idx, selected, banned_id, user_id):
    if idx == len(banned_id):
        answer_set.add(selected)
        return

    for i in range(len(user_id)):
        if not 1 << i & selected:
            if len(banned_id[idx]) != len(user_id[i]):
                continue

            for j in range(len(banned_id[idx])):
                if banned_id[idx][j] != user_id[i][j] and banned_id[idx][j] != "*":
                    break
            else:
                selected += 1 << i
                check(idx + 1, selected, banned_id, user_id)
                selected -= 1 << i


def solution(user_id, banned_id):
    global answer_set

    selected = 0
    answer_set = set()
    check(0, selected, banned_id, user_id)
    return len(answer_set)


print(solution(user_id, banned_id))