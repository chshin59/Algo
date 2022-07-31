enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

# enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller = ["sam", "emily", "jaimie", "edward"]
# amount = [2, 3, 5, 4]


def func(seller, money):
    global answer_d
    if seller == 'root':
        return

    if money * 0.1 < 1:
        answer_d[seller] += money
        return

    answer_d[seller] += money - int(money * 0.1)
    func(parent_d[seller], int(money * 0.1))


def solution(enroll, referral, seller, amount):
    global answer_d, parent_d
    for i in range(len(enroll)):
        answer_d[enroll[i]] = 0
        if referral[i] != "-":
            parent_d[enroll[i]] = referral[i]
        else:
            parent_d[enroll[i]] = "root"

    for i in range(len(seller)):
        func(seller[i], amount[i] * 100)

    answer = []
    for i in range(len(enroll)):
        answer.append(answer_d[enroll[i]])

    return answer


answer_d = dict()
parent_d = dict()
print(solution(enroll, referral, seller, amount))