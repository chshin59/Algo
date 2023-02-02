def bigger(idx):
    cnt = 1
    for j in range(N):
        if people[j][0] > people[idx][0] and people[j][1] > people[idx][1]:
            cnt += 1
    return cnt


N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

cnt_list = []

for i in range(N):
    cnt_list.append(bigger(i))

print(' '.join(map(str, cnt_list)))
