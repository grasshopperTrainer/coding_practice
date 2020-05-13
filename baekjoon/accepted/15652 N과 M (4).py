def solution(N, M):

    def permutatioin(pool, l, selected=[]):
        if len(selected) == l:
            return [selected]

        record = []
        for n in pool:
            if not selected or selected[-1] <= n:
                record += permutatioin(pool, l, selected + [n])
        return record

    return permutatioin(range(1, N+1), M)


N, M = [int(c) for c in input().strip().split(' ')]
for nums in solution(N, M):
    print(' '.join([str(i) for i in nums]))