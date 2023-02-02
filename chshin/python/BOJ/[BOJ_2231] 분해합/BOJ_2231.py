N = input()
digit = len(list(N))

N = int(N)

def digit_generator():
    if N-9*digit < 1:
        start = 1
    else:
        start = N-9*digit
        
    for i in range(start, N):
        tmp = 0
        j = i
        for _ in range(digit):
            tmp += j % 10
            j //= 10
        
        if tmp + i == N:
            return i

if digit_generator() is None:
    print(0)
else:
    print(digit_generator())

# N = input()
# digit = len(N)

# N = int(N)
# generator = 0
# for i in range(1, N):
#     tmp = i
#     total = i
#     for _ in range(digit):
#         total += tmp % 10
#         tmp //= 10
#     if total == N:
#         generator = i
#         break
# print(generator)