import sys
sys.stdin = open('input.txt')

def is_different(lst):
    for i in range(len(tmp_list)):
        for j in range(i+1, len(tmp_list)):
            if lst[i] == lst[j]:
                return False
    return True


N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    len(word)

    tmp_list = [word[0]]
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            tmp_list.append(word[i])
    
    if is_different(tmp_list):
        cnt += 1

print(cnt)
