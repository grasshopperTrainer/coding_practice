from sys import stdin, setrecursionlimit


setrecursionlimit(100000)
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
        return root + build(left_in_d, left_post_d) + build(right_in_d, right_post_d)
    try:
       return build([0, N], [0, N])
    except:
        raise


# N, inorder, postorder = 0, [], []
# for i, row in enumerate(stdin.readlines()):
#     if i == 0:
#         N = int(row)
#     elif i == 1:
#         inorder = row.strip().split(' ')
#     else:
#         postorder = row.strip().split(' ')
#
# print(' '.join(solution(N, inorder, postorder)))

import random
from collections import deque
def build_binary_tree(elements):
    random.shuffle(elements)
    origin = elements.pop()
    roots = deque([origin])
    tree = {}

    while elements:
        random.shuffle(roots)
        root = roots.popleft()
        # how many children?
        children = [elements.pop() for _ in range(random.randint(0, 2)) if elements]
        if not children:
            roots.append(root)
        elif len(children) == 1:
            tree[root] = [children[0], None]
            roots.append(children[0])
        else:
            tree[root] = children
            roots.append(children[1])

    return tree, origin

def traversal(tree, root):
    if root is None:
        return [], [], []
    if root not in tree:
        return [root], [root], [root]
    lefts = traversal(tree, tree[root][0])
    rights = traversal(tree, tree[root][1])

    front = [root] + lefts[0] + rights[0]
    middle = lefts[1] + [root] + rights[1]
    end = lefts[2] + rights[2] + [root]
    return front, middle, end

while True:

    try:
        origin = random.randint(1, 10)
        N = random.randint(1, 10_000)
        t, o = build_binary_tree(list(range(origin, origin+N)))
        # try:
        pre_order, in_order, post_order = [[str(c) for c in l] for l in traversal(t, o)]
        # except:
        # print('fail traversaling')
        print('g')
    except:
        raise
    #     answer = solution(N, in_order, post_order)
    #     if answer != ''.join([str(c) for c in pre_order]):
    #         print(answer)
    #         print(pre_order)
    #         print('bad')
    #         exit()
    #     print('good')
    #
    # except Exception as e:
    #     print('bad')
    #     # print(t)
    #     # print(pre_order)
    #     # print(in_order)
    #     # print(post_order)
    #     raise(e)
"""
2
1 2
2 1
"""
"""
5
2 4 1 5 3
4 2 5 3 1

1 2 4 3 5
"""
"""
5
3 4 5 2 1
5 4 3 2 1

1 2 3 4 5
"""
"""
4
1 2 3 4
4 3 2 1

1 2 3 4
"""
'''
5
4 2 1 3 5
4 2 5 3 1

1 2 4 3 5
'''