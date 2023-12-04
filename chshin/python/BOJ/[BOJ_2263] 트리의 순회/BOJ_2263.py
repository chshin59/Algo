import sys
sys.setrecursionlimit(200000)
sys.stdin = open('input.txt')


def solve(inorder_start_idx, inorder_end_idx, postorder_start_idx, postorder_end_idx, n):
    tmp = postorder[postorder_end_idx]
    preorder.append(tmp)
    idx = position[tmp]

    left_cnt = idx - inorder_start_idx
    right_cnt = inorder_end_idx - idx

    if n == 1:
        return

    if left_cnt > 0:
        solve(inorder_start_idx, inorder_start_idx + left_cnt - 1, postorder_start_idx, postorder_start_idx + left_cnt - 1, left_cnt)

    if right_cnt > 0:
        solve(inorder_end_idx - right_cnt + 1, inorder_end_idx, postorder_end_idx - right_cnt, postorder_end_idx - 1, right_cnt)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0] * (n + 1)
for i in range(n):
    position[inorder[i]] = i

preorder = []
solve(0, n - 1 , 0, n - 1, n)
print(' '.join(map(str, preorder)))
