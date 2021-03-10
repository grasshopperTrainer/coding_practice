from sys import stdin, setrecursionlimit

setrecursionlimit(300_000)
def solution(N, weights, supervisors):
    ROOT = 1

    graph = {}
    for i, s in enumerate(supervisors, 2):
        graph.setdefault(s, []).append(i)

    def fill_dp(at):
        if not graph.get(at, []):
            return [weights[at-1], 0], [at], []

        summed = [weights[at-1], 0]
        A, B = [at], []
        for child in graph[at]:
            vs, a, b = fill_dp(child)
            max_v = max(vs)
            if 0 < max_v:
                summed[1] += max_v
                if vs[0] < vs[1]:
                    B += b
                else:
                    B += a
            if 0 < vs[1]:
                summed[0] += vs[1]
                A += b
        return summed, A, B

    count, select_root, select_root_not = fill_dp(ROOT)
    select_root.sort()
    select_root_not.sort()

    print(' '.join(map(str, count)))
    print(' '.join(map(str, select_root+[-1])))
    print(' '.join(map(str, select_root_not+[-1])))


N = int(stdin.readline())
weights = [int(c) for c in stdin.readline().strip().split(' ')]
supervisors = [int(c) for c in stdin.readline().strip().split(' ')]

solution(N, weights, supervisors)