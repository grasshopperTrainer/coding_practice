# very slow solution
# simpler is faster
from sys import stdin


def solution(N, K, queries):
    if K == 1:  # critical
        for a, b in queries:
            print(abs(a - b))
        return

    def mother_of(n):
        if n == 1:
            return 1
        return (n + (K - 2)) // K

    def depth_of(N):
        # this function is needless, small N always has less depth
        n = N
        depth = 0
        while n != 1:
            n = (n + (K - 2)) // K
            depth += 1
        return depth

    ancestors = {}
    def ancestor_of(n, idx):
        if n in ancestors and idx in ancestors[n]:
            return ancestors[n][idx]

        if idx == 0:
            ancestors.setdefault(n, {})[0] = mother_of(n)
            return ancestors[n][0]
        ancestor = ancestor_of(ancestor_of(n, idx - 1), idx - 1)
        ancestors.setdefault(n, {})[idx] = ancestor
        return ancestor

    # find lca
    for a, b in queries:
        dist = 0
        while depth_of(a) != depth_of(b):
            anc = 0
            if depth_of(a) < depth_of(b):
                while depth_of(a) < depth_of(ancestor_of(b, anc + 1)):
                    anc += 1
                b = ancestor_of(b, anc)
            else:
                while depth_of(ancestor_of(a, anc + 1)) > depth_of(b):
                    anc += 1
                a = ancestor_of(a, anc)
            dist += 2 ** anc

        if a == b:
            print(dist)
            continue

        while ancestor_of(a, 0) != ancestor_of(b, 0):
            anc = 0
            while True:
                if ancestor_of(a, anc) != ancestor_of(b, anc):
                    anc += 1
                else:
                    anc -= 1
                    break
            dist += 2 ** (anc + 1)
            a, b = ancestor_of(a, anc), ancestor_of(b, anc)

        dist += 2
        print(dist)


N, K, Q = map(int, stdin.readline().strip().split(' '))
queries = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(Q)]

solution(N, K, queries)

# print((4+13)**(1/3))
"""
9 3 0
"""
"""
1000000000000000 1 1
1545454646 659785451
"""
