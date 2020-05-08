from sys import stdin


def solution(N, M, trees):

    def tree_cut(l):
        count = 0
        for t in trees:
            count += max([0, t-l])
        return count

    s, e = 0, 1_000_000_000
    while s <= e:
        m = (s+e)//2
        if tree_cut(m) >= M:    # set max height
            s = m + 1
        else:
            e = m - 1
    return e


N, M, trees = 0, 0, []
for i,row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M = row
    else:
        trees = row

print(solution(N, M, trees))