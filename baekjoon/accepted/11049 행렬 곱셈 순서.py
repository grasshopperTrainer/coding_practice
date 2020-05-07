from sys import stdin

def solution(N, matrices):
    MAX, NORECORD = 2**31, -1
    # not Python but PyPy solves in time
    # using dict with tuple key (ex: cache[(x, y)]) is timeout
    # think this is due to time consumed by generating hash
    # !!! if search space is relatively small, always use 2D list !!!
    cache = [[NORECORD for _ in range(500)] for _ in range(500)]
    def calc(s, e):
        if cache[s][e] != NORECORD:
            return cache[s][e]
        if s == e:
            cache[s][e] = 0
            return 0

        min_sum = MAX
        for m in range(s, e):
            min_sum = min([min_sum, calc(s, m) + calc(m+1, e) + matrices[s][0]*matrices[m][1]*matrices[e][1]])
        cache[s][e] = min_sum
        return min_sum

    return calc(0, N-1)


N, matrices = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        matrices.append([int(c) for c in row.strip().split(' ')])

print(solution(N, matrices))