from sys import stdin, setrecursionlimit

setrecursionlimit(20_000)
def solution(N, inorder, postorder):

    in_idx = {e: i for i, e in enumerate(inorder)}

    def build(in_domain, post_domain):
        if in_domain[0] == in_domain[1]:
            return ''
        elif in_domain[0]+1 == in_domain[1]:
            return inorder[in_domain[0]]

        root_idx = post_domain[-1] - 1
        root = postorder[root_idx]
        in_root_idx = in_idx[root]
        in_left_len = in_root_idx - in_domain[0]

        left_in_d = in_domain[0], in_root_idx
        left_post_d = post_domain[0], post_domain[0]+in_left_len
        right_in_d = in_root_idx+1, in_domain[1]
        right_post_d = post_domain[0]+in_left_len, post_domain[1] - 1
        # print(in_domain, post_domain)
        # print(left_in_d, left_post_d, right_in_d, right_post_d)
        return root + build(left_in_d, left_post_d) + build(right_in_d, right_post_d)

    return build([0, N], [0, N])


N, inorder, postorder = 0, [], []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    elif i == 1:
        inorder = row.strip().split(' ')
    else:
        postorder = row.strip().split(' ')

print(' '.join(solution(N, inorder, postorder)))
