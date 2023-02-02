import sys
sys.stdin = open('input.txt')


def repaint():
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and board_cut[i][j] == 'B':
                cnt += 1
            if (i+j) % 2 == 1 and board_cut[i][j] == 'W':
                cnt += 1
    if cnt <= 32:
        return cnt
    else:
        return 64-cnt

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

answer = 64
for i in range(N-7):
    for j in range(M-7):
        # board_cut 생성
        board_cut = []
        for k in range(8):
            board_cut.append(board[i+k][j:j+8])

        # answer 보다 작으면 교체
        if repaint() < answer:
            answer = repaint()
print(answer)