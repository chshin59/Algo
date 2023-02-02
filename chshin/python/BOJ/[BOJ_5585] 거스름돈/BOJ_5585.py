M = 1000 - int(input())

changes = [500, 100, 50, 10, 5, 1]
answer = 0
for change in changes:
    if M // change > 0:
        answer += M // change
        M %= change
    if M == 0:
        break
print(answer)