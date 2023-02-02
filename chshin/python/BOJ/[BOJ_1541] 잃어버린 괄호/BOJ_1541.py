import sys

sys.stdin = open('input.txt')


expression = input()

new_expression = ''
for i in expression:
    if i == '+':
        new_expression += ' + '
    elif i == '-':
        new_expression += ' - '
    else:
        new_expression += i

new_expression = new_expression.split(' ')

sign = '+'
answer = 0
for j in new_expression:
    if j =='-':
        sign = '-'
    elif j == '+':
        pass
    else:
        answer = answer + int(j) if sign == '+' else answer - int(j)
print(answer)
