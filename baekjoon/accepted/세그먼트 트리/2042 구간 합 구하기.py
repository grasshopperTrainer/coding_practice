from sys import stdin, setrecursionlimit

setrecursionlimit(5000)


def solution(N, nums, insts):
    REPLACE, PRINT = 1, 2

    tree_size = 2 ** int(len(bin(len(nums))[2:])+1) # ceiling 2**n
    nodes = [0]*tree_size
    def build_sum_tree(start, end, idx=1):
        if start == end:
            nodes[idx] = nums[start]
        else:
            mid = (end+start)//2
            nodes[idx] = build_sum_tree(start, mid, idx*2) + build_sum_tree(mid+1, end, idx*2+1)
        return nodes[idx]

    def calc_cum(start, end, left, right, idx=1):
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return nodes[idx]
        else:
            mid = (start + end) // 2
            return calc_cum(start, mid, left, right, idx * 2) + calc_cum(mid + 1, end, left, right, idx * 2 + 1)

    def replace_value(start, end, val_idx, delta, node_idx=1):
        if start == val_idx == end:
            nodes[node_idx] += delta
        elif start <= val_idx <= end:
            mid = (start + end) // 2
            nodes[node_idx] = replace_value(start, mid, val_idx, delta, node_idx*2) + replace_value(mid+1, end, val_idx, delta, node_idx*2+1)
        return nodes[node_idx]

    # build
    build_sum_tree(0, N-1)
    # run instruction
    for inst in insts:
        if inst[0] == REPLACE:
            _, i, v = inst
            delta = v - nums[i-1]
            nums[i-1] = v
            replace_value(0, N-1, i-1, delta)
        elif inst[0] == PRINT:
            _, l, r = inst
            print(calc_cum(0, N-1, l-1, r-1))



nums = []
insts = []
N = 0
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N, _, _ = [int(c) for c in row.strip().split(' ')]
    elif i <= N:
        nums.append(int(row))
    else:
        insts.append([int(c) for c in row.strip().split(' ')])

solution(N, nums, insts)
