import sys
sys.stdin = open('input.txt')

infix = input()
stack = []
rank = {
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
    "(": 0,
    ")": 0
}

for idx in range(len(infix)):
    if infix[idx] == "(":
        stack.append(infix[idx])
    elif infix[idx] == ")":
        while stack[-1] != "(":
            print(stack[-1], end="")
            stack.pop()
        stack.pop()
    elif infix[idx] in ["*", "/", "+", "-"]:
        while stack and rank[stack[-1]] >= rank[infix[idx]]:
            print(stack[-1], end="")
            stack.pop()
        stack.append(infix[idx])
    else:
        print(infix[idx], end="")
        
while stack:
    print(stack[-1], end="")
    stack.pop()
