def solution(n, k):
    nn = ''
    while n // k or n % k:
        nn = str(n % k) + nn
        n = n // k
    lst = nn.split('0')
    print(lst)

    def is_prime(x):
        x = int(x)
        if x == 1:
            return False

        k = 2
        while x // k >= k:
            if x % k == 0:
                return False
            k += 1
        return True

    answer = 0
    for number in lst:
        if number and is_prime(number):
            answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
