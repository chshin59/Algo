from collections import deque


drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]


def bfs(position1, position2, board):
    if position1 == position2:
        return 0

    cnt = 0
    visited = set()
    visited.add(tuple(position1))
    dq = deque([position1])

    while True:
        n = len(dq)
        cnt += 1
        for _ in range(n):
            r1, c1 = dq.popleft()
            for d in range(4):
                r2, c2 = r1, c1
                # ctrl 이동
                while True:
                    r2 += drs[d]
                    c2 += dcs[d]
                    if not 0 <= r2 < 4 or not 0 <= c2 < 4:
                        break
                    if board[r2][c2] or (d, r2) in [(0, 3), (2, 0)] or (d, c2) in [(1, 3), (3, 0)]:
                        if (r2, c2) not in visited:
                            dq.append([r2, c2])
                            visited.add((r2, c2))
                        break

                # 1칸 이동
                r2, c2 = r1 + drs[d], c1 + dcs[d]
                if 0 <= r2 < 4 and 0 <= c2 < 4:
                    if (r2, c2) not in visited:
                        dq.append([r2, c2])
                        visited.add((r2, c2))

            if position2 in dq:
                return cnt


def dfs(chars, now, move, board):
    global answer
    # 종료조건
    if not chars:
        if move < answer:
            answer = move
        return

    # 가지치기
    if move > answer:
        return

    n = len(chars)
    for i in range(n):
        j = i // 2 * 2 if i % 2 else i + 1

        first, second = chars[i], chars[j]
        new_move = move

        # 거리
        new_move += bfs(now, first[1:], board)
        board[first[1]][first[2]] = 0

        new_move += bfs(first[1:], second[1:], board)
        board[second[1]][second[2]] = 0

        new_chars = chars[:min(i, j)] + chars[max(i, j) + 1:]

        dfs(new_chars, second[1:], new_move, board)

        # 초기화
        board[first[1]][first[2]] = first[0]
        board[second[1]][second[2]] = second[0]


def solution(board, r, c):
    global answer, move
    chars = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                chars.append([board[i][j], i, j])
    chars.sort()

    answer = float('inf')
    dfs(chars, [r, c], 0, board)

    return answer + len(chars)


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
# 14
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
# 16

# print(bfs([1, 0], [2, 3], [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]))
