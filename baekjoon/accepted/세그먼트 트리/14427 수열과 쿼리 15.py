from sys import stdin


def solution(N, nums, queries):
    LEAF_SIZE = 2 ** len(bin(N-1)[2:])
    tree = [0]*LEAF_SIZE*2

    def fill_tree(left, right, tree_idx, val_idx):
        if left == right:
            tree[tree_idx] = val_idx
            return tree[tree_idx]
        m = (left+right)//2
        if val_idx <= m:
            a = fill_tree(left, m, tree_idx*2, val_idx)
            b = tree[tree_idx*2+1]
        else:
            a = tree[tree_idx*2]
            b = fill_tree(m+1, right, tree_idx*2+1, val_idx)
        tree[tree_idx] = sorted((a, b), key=lambda x: nums[x-1])[0]
        return tree[tree_idx]

    for i in range(1, N+1):
        fill_tree(1, LEAF_SIZE, 1, i)

    answers = []
    for query in queries:
        if query == [2]:
            answers.append(tree[1])
            continue
        _, i, v = query
        nums[i-1] = v
        fill_tree(1, LEAF_SIZE, 1, i)
    return answers


N = int(stdin.readline())
nums = [int(c) for c in stdin.readline().strip().split(' ')]
M = int(stdin.readline())
queries = []
for _ in range(M):
    queries.append([int(c) for c in stdin.readline().strip().split(' ')])
for a in solution(N, nums, queries):
    print(a)