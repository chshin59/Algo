import sys
sys.stdin = open('input.txt')

N1 = int(input())
switches = list(map(int, input().split()))
N2 = int(input())

for _ in range(N2):
    G, N3 = map(int, input().split())
    # 남자
    if G == 1:
        # for문 한번 돌면서 배수인것만 += 1
        for i in range(N1):
            if (i+1) % N3 == 0:
                switches[i] = (switches[i] + 1) % 2
    # 여자
    else:
        j = N3 - 1
        # 자기 위치 += 1
        switches[j] = (switches[j] + 1) % 2
        L, R = j - 1, j + 1
        # 좌우로 이동하면서 대칭여부 확인후 += 1
        while 0 <= L and R <= N1 - 1:
            if switches[L] == switches[R]:
                switches[L], switches[R] = (switches[L] + 1) % 2, (switches[R] + 1) % 2
                L, R = L-1, R+1
            else:
                break

# 출력 20개씩
N4 = (N1 - 1) // 20
for k in range(N4):
    print(' '.join(list(map(str, switches[k * 20:(k + 1) * 20]))))
print(' '.join(list(map(str, switches[N4 * 20:]))))
