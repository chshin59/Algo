import sys
sys.stdin = open('input.txt')


def dfs(selected, idx):
    if idx == n:
        if not selected:
            return
        else:
            answer = list(formula)
            for idx in selected:
                answer[idx] = ''
            answer_set.add(''.join(answer))
            return
    
    dfs(selected, idx + 1)
    dfs(selected + pairs[idx], idx + 1)

formula = input()
pairs = []
stack = []
for idx in range(len(formula)):
    if formula[idx] == '(':
        stack.append(idx)
    elif formula[idx] == ')':
        pairs.append([stack.pop(), idx])

n = len(pairs)

answer_set = set()
dfs([], 0)
for answer in sorted(answer_set):
    print(answer)
