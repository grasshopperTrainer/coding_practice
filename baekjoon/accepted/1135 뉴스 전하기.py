from sys import stdin


def solution(N, bosses):
    # draw tree
    tree = [[] for _ in range(N)]
    for employee, boss in enumerate(bosses[1:], 1):
        tree[boss].append(employee)

    def search(idx):
        if not tree[idx]:
            return 0

        r = [search(e) for e in tree[idx]]
        r.sort(reverse=True)
        return max(i+v for i, v in enumerate(r, 1))

    return search(0)


N = int(stdin.readline())
bosses = list(map(int, stdin.readline().strip().split(' ')))

print(solution(N, bosses))

"""
9
-1 0 0 0 1 1 3 3 7
"""
