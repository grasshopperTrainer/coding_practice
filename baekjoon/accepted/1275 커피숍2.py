from sys import stdin


def solution(N, Q, nums, instructions):
    num_leaf = 2**len(bin(N)[2:])
    num_tree = num_leaf*2
    tree = [0 for _ in range(num_tree)]

    def fill_tree(left, right, idx):
        if left == right:
            if left <= N:
                tree[idx] = nums[left-1]
            return tree[idx]

        m = (left+right)//2
        tree[idx] = fill_tree(left, m, idx*2) + fill_tree(m+1, right, idx*2+1)
        return tree[idx]

    fill_tree(1, num_leaf, 1)

    def replace_tree(left, right, tree_idx, num_idx):
        if left == right:
            if left == num_idx:
                tree[tree_idx] = nums[num_idx-1]
            return tree[tree_idx]

        m = (left+right)//2
        if num_idx <= m:
            a, b = replace_tree(left, m, tree_idx*2, num_idx), tree[tree_idx*2+1]
        else:
            a, b = tree[tree_idx*2], replace_tree(m+1, right, tree_idx*2+1, num_idx)
        tree[tree_idx] = a + b
        return tree[tree_idx]

    def calc_seg(left, right, start, end, tree_idx):
        if start <= left and right <= end:
            return tree[tree_idx]
        if end < left or right < start:
            return 0
        m = (left+right)//2
        return calc_seg(left, m, start, end, tree_idx*2) + calc_seg(m+1, right, start, end, tree_idx*2+1)

    answers = []
    for x, y, a, b in instructions:
        x, y = sorted([x, y])
        answers.append(calc_seg(1, num_leaf, x, y, 1))
        nums[a-1] = b
        replace_tree(1, num_leaf, 1, a)
        # print(tree)
    return answers


def parse(): return [int(c) for c in stdin.readline().strip().split(' ')]
N, Q = parse()
nums = parse()
instructions = [parse() for _ in range(Q)]

for a in solution(N, Q, nums, instructions):
    print(a)