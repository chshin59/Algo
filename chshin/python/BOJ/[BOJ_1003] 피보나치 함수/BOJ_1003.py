def func(num_list):
    max_num = max(num_list)
    zero_one = [[1, 0], [0, 1]]
    if max_num >= 2:
        for _ in range(2, max_num + 1):
            zero_one.append([zero_one[-1][0] + zero_one[-2][0], zero_one[-1][1] + zero_one[-2][1]])
    for num in num_list:
        print(' '.join(map(str, zero_one[num])))


T = int(input())
numbers = []
for _ in range(1, T + 1):
    numbers.append(int(input()))

func(numbers)
