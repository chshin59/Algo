import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
meetings = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    meetings.append((start, end))

meetings = sorted(meetings, key=lambda x: x[1])
meetings = sorted(meetings, key=lambda x: x[0])

answer = [(-1, -1)]
for meeting in meetings:
    if meeting[0] == meeting[1]:
        if meeting[0] < answer[-1][1]:
            answer.pop()
        answer.append(meeting)
    else:
        if meeting[0] <= answer[-1][1] and meeting[1] <= answer[-1][1]:
            answer.pop()
        if meeting[0] >= answer[-1][1]:
            answer.append(meeting)

print(len(answer)-1)
