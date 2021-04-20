from sys import stdin


def change_val(idx, val, left, right, tid, tree):
    if left == right:
        tree[tid] = val
        return val

    m = (left + right) // 2
    if idx <= m:
        tree[tid] = min(change_val(idx, val, left, m, tid * 2, tree), tree[tid * 2 + 1])
    else:
        tree[tid] = min(tree[tid * 2], change_val(idx, val, m + 1, right, tid * 2 + 1, tree))
    return tree[tid]


def search_min(start, end, left, right, tid, tree):
    if right < start or end < left:
        return float('inf')
    if start <= left and right <= end:
        return tree[tid]

    m = (left + right) // 2
    left_min = search_min(start, end, left, m, tid * 2, tree)
    right_min = search_min(start, end, m + 1, right, tid * 2 + 1, tree)
    return min(left_min, right_min)


def solution(N, seq, queries):
    # init
    NLEAF = 2 ** (len(bin(N)[2:]))
    st = [float('inf')] * NLEAF * 2
    for i, n in enumerate(seq, 1):
        change_val(i, n, left=1, right=NLEAF, tid=1, tree=st)

    # query
    for t, a, b in queries:
        if t == 1:
            change_val(idx=a, val=b, left=1, right=NLEAF, tid=1, tree=st)
        else:
            print(search_min(start=a, end=b, left=1, right=NLEAF, tid=1, tree=st))


N = int(stdin.readline())
seq = list(map(int, stdin.readline().strip().split(' ')))
M = int(stdin.readline())
queries = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]

solution(N, seq, queries)
