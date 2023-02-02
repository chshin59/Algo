import sys
sys.stdin = open('input.txt')


def counting(bd_idx, buildings):
    cnt = 0
    if bd_idx > 0:
        # 좌측 탐색
        i = bd_idx - 1
        slope = (buildings[i] - buildings[bd_idx]) / (i - bd_idx)

        cnt += 1
        i -= 1
        while i >= 0:
            slope_c = (buildings[i] - buildings[bd_idx]) / (i - bd_idx)
            if slope > slope_c:
                slope = slope_c
                cnt += 1
            i -= 1
    
    if bd_idx < N-1:
        # 우측 탐색
        j = bd_idx + 1
        slope = (buildings[j] - buildings[bd_idx]) / (j - bd_idx)

        cnt += 1
        j += 1
        while j <= N - 1:
            slope_c = (buildings[j] - buildings[bd_idx]) / (j - bd_idx)
            if slope < slope_c:
                slope = slope_c
                cnt += 1
            j += 1
    
    return cnt


N = int(input())
buildings = list(map(int, input().split()))

cnt_list = []

for idx in range(N):
    cnt_list.append(counting(idx, buildings))

answer = 0
for cnt in cnt_list:
    if answer < cnt:
        answer = cnt
print(answer)
