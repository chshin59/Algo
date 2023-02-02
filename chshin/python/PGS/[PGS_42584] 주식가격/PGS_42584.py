prices = [1, 2, 3, 2, 3]


def solution(prices):
    n = len(prices)
    stack = []
    answer = [0] * n
    prices[-1] = -1

    for idx in range(n - 1):
        stack.append(idx)
        while stack and prices[stack[-1]] > prices[idx + 1]:
            tmp = stack.pop()
            answer[tmp] = idx + 1 - tmp
    
    return answer


print(solution(prices))
