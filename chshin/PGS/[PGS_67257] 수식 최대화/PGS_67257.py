from itertools import permutations


expression = "100-200*300-500+20"
# expression = "50*6-3*2"


def cal(arr, sign):
    arr2 = []
    if sign == "+":
        for i in range(len(arr)):
            if i % 2 and arr[i] == "+":
                arr[i + 1] = arr2.pop() + arr[i + 1]
            elif i % 2:
                arr2.append(arr[i])
            else:
                arr2.append(arr[i])
    elif sign == "-":
        for i in range(len(arr)):
            if i % 2 and arr[i] == "-":
                arr[i + 1] = arr2.pop() - arr[i + 1]
            elif i % 2:
                arr2.append(arr[i])
            else:
                arr2.append(arr[i])
    elif sign == "*":
        for i in range(len(arr)):
            if i % 2 and arr[i] == "*":
                arr[i + 1] = arr2.pop() * arr[i + 1]
            elif i % 2:
                arr2.append(arr[i])
            else:
                arr2.append(arr[i])
    return arr2


def solution(expression):
    expression = expression.replace("-", " - ")
    expression = expression.replace("+", " + ")
    expression = expression.replace("*", " * ")
    arr = expression.split(" ")
    for i in range(len(arr)):
        if not i % 2:
            arr[i] = int(arr[i])

    answer = 0
    for p in permutations(["+", "-", "*"]):
        tmp = arr[:]
        for i in range(3):
            tmp = cal(tmp, p[i])
            print(tmp)
        print()
        answer = max(answer, abs(tmp[0]))
    return answer


print(solution(expression))
