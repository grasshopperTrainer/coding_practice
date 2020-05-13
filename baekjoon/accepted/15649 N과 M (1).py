def solution(N, M):

    def permutation(pool, l, visited=set(), selection=[]):
        if len(selection) == l:
            return [selection]

        record = []
        for i, n in enumerate(pool):
            if i not in visited:
                visited.add(i)
                record += permutation(pool, l, visited, selection + [n])
                visited.remove(i)
        return record

    return permutation(list(range(1, N+1)), M)


N, M = [int(c) for c in input().strip().split(' ')]
for ns in solution(N, M):
    print(' '.join([str(i) for i in ns]))