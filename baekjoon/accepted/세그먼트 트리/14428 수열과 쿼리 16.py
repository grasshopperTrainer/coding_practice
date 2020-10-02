from sys import stdin, setrecursionlimit

setrecursionlimit(100_100)


def solution(N, vals, queries):
    LEAF_SIZE = 2**len(bin(N-1)[2:])
    tree = [None]*2*LEAF_SIZE

    def fill_tree(left, right, tid):
        if left == right:
            if left <= N:
                tree[tid] = left
            return tree[tid]
        m = (left + right)//2
        idxs = (fill_tree(left, m, tid * 2), fill_tree(m + 1, right, tid * 2 + 1))
        tree[tid] = sorted(idxs, key=lambda x: vals[x-1] if x is not None else float('inf'))[0]
        return tree[tid]
    fill_tree(1, LEAF_SIZE, 1)

    def update_tree(left, right, tid, idx):
        if left == right:
            return tree[tid]

        m = (left + right)//2
        if idx <= m:
            a = update_tree(left, m, tid*2, idx)
            b = tree[tid*2+1]
        else:
            a = tree[tid*2]
            b = update_tree(m+1, right, tid*2+1, idx)
        tree[tid] = sorted((a, b), key=lambda x: vals[x-1] if x is not None else float('inf'))[0]
        return tree[tid]

    def query_min(left, right, start, end, tid):
        if start <= left and right <= end:
            return tree[tid]
        if end < left or right < start:
            return None
        m = (left + right)//2
        idxs = query_min(left, m, start, end, tid * 2), query_min(m + 1, right, start, end, tid * 2 + 1)
        return sorted(idxs, key=lambda x: vals[x-1] if x is not None else float('inf'))[0]

    answers = []
    for op, a, b in queries:
        if op == 1:
            vals[a-1] = b
            update_tree(1, LEAF_SIZE, 1, a)
        elif op == 2:
            answers.append(query_min(1, LEAF_SIZE, a, b, 1))
    return answers


lexer = lambda: [int(c) for c in stdin.readline().strip().split(' ')]
N = int(stdin.readline())
vals = lexer()
M = int(stdin.readline())
queries = [lexer() for _ in range(M)]

for a in solution(N, vals, queries):
    print(a)
