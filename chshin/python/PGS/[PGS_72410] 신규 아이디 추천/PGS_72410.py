def function2(string):
    if string.islower() or string.isdigit():
        return string
    if string == "-" or string == "_" or string == ".":
        return string
    else:
        return ""


def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    new_id = ''.join(list(map(function2, list(new_id))))

    # 3
    tmp = new_id[:1]
    for i in range(1, len(new_id)):
        if not (new_id[i] == "." and new_id[i-1] == "."):
            tmp += new_id[i]
    new_id = tmp

    # 4
    new_id = new_id.strip(".")

    # 5
    if new_id == "":
        new_id += "a"

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15].strip(".")

    # 7
    if len(new_id) <= 2:
        tmp = new_id[-1]
        while len(new_id) < 3:
            new_id += tmp

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))