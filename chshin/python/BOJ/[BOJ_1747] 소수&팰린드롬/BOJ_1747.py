def is_prime(n):
    for i in range(-int(-n ** 0.5 // 1), n):
        if not n % i:
            return False
    return True


def is_palindrome(n):
    return list(str(n)) == list(str(n)[::-1])


N = int(input())
if N <= 2:
    print(2)
else:
    if N % 2 == 0:
        N += 1
    while not (is_palindrome(N) and is_prime(N)):
        N += 2
    print(N)
