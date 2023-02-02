def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    tmp = [[0] * (M + 1) for _ in range(N + 1)]  # 누적합 기록을 위한 배열

    for heal, r1, c1, r2, c2, degree in skill:
        # type (attack = 1, heal = 2)
        # 누적합 기록, 부호에 주의할 것
        tmp[r1][c1] += degree if heal == 2 else -degree
        tmp[r1][c2 + 1] += -degree if heal == 2 else degree
        tmp[r2 + 1][c1] += -degree if heal == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if heal == 2 else -degree

    # 행 기준 누적합
    for i in range(N):
        for j in range(M):
            tmp[i][j + 1] += tmp[i][j]

    # 열 기준 누적합
    for j in range(M):
        for i in range(N):
            tmp[i + 1][j] += tmp[i][j]

    # 기존 배열과 합함
    for i in range(N):
        for j in range(M):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer += 1
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution([[5,5,5,5,5],[5,5,5,5, 5],[5,5,5,5,5],[5,5,5,5,5]],
               [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
