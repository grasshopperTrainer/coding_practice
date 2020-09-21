from sys import stdin


def put(left, right, tree_idx, tree, min_max, num_idx, nums):
    if left == right:
        tree[tree_idx] = nums[num_idx]
        return tree[tree_idx]

    m = (left + right) // 2
    if num_idx < m:
        if min_max:
            tree[tree_idx] = max(tree[tree_idx], put(left, m, tree_idx * 2, tree, min_max, num_idx, nums))
        else:
            tree[tree_idx] = min(tree[tree_idx], put(left, m, tree_idx * 2, tree, min_max, num_idx, nums))
    else:
        if min_max:
            tree[tree_idx] = max(tree[tree_idx], put(m + 1, right, tree_idx * 2 + 1, tree, min_max, num_idx, nums))
        else:
            tree[tree_idx] = min(tree[tree_idx], put(m + 1, right, tree_idx * 2 + 1, tree, min_max, num_idx, nums))
    return tree[tree_idx]


def get(left, right, start, end, min_max, tree_idx, tree):
    if start <= left and right <= end:
        return tree[tree_idx]
    elif end < left or right < start:
        if min_max:
            return 0
        else:
            return float('inf')

    m = (left + right) // 2
    if min_max:
        return max(get(left, m, start, end, min_max, tree_idx * 2, tree),
                   get(m + 1, right, start, end, min_max, tree_idx * 2 + 1, tree))
    else:
        return min(get(left, m, start, end, min_max, tree_idx * 2, tree),
                   get(m + 1, right, start, end, min_max, tree_idx * 2 + 1, tree))


def solution(N, M, nums, bounds):
    BLOCK_SIZE = 2 ** len(bin(N)[2:])

    min_tree = [float('inf')] * 2 * BLOCK_SIZE
    max_tree = [0] * 2 * BLOCK_SIZE

    for i in range(N):
        put(1, BLOCK_SIZE, 1, min_tree, 0, i, nums)
        put(1, BLOCK_SIZE, 1, max_tree, 1, i, nums)

    answers = []
    for start, end in bounds:
        answers.append([get(1, BLOCK_SIZE, start, end, 0, 1, min_tree), get(1, BLOCK_SIZE, start, end, 1, 1, max_tree)])
    return answers


N, M = map(int, stdin.readline().strip().split(' '))
nums, bounds = [], []
for _ in range(N):
    nums.append(int(stdin.readline()))
for _ in range(M):
    bounds.append(list(map(int, stdin.readline().strip().split(' '))))

for a in solution(N, M, nums, bounds):
    print(' '.join(map(str, a)))
