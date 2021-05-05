from sys import stdin


def solution(N, M, ranks, changes):
    counts = {}
    win_over = [[] for _ in range(N)]
    changed = {}
    for a, b in changes:
        a, b = a - 1, b - 1
        changed.setdefault(a, set()).add(b)
        changed.setdefault(b, set()).add(a)

    for i in range(N):
        for j in range(i + 1, N):
            a, b = ranks[i] - 1, ranks[j] - 1
            if b in changed.get(a, set()):
                a, b = b, a
            win_over[a].append(b)
            counts[b] = counts.get(b, 0) + 1

    new_rank = []
    winners = []
    for i in range(N):
        if i not in counts:
            winners.append(i)

    if not winners:
        return 'IMPOSSIBLE'
    if 1 < len(winners):
        return '?'

    winner = winners[0]
    new_rank.append(winner+1)
    for _ in range(N-1):
        winners = []
        for losser in win_over[winner]:
            counts[losser] -= 1
            if counts[losser] == 0:
                winners.append(losser)

        if not winners:
            return 'IMPOSSIBLE'
        if 1 < len(winners):
            return '?'
        winner = winners[0]
        new_rank.append(winner+1)

    return ' '.join(map(str, new_rank))


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    ranks = tuple(map(int, stdin.readline().strip().split(' ')))
    M = int(stdin.readline())
    changes = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]

    print(solution(N, M, ranks, changes))

"""
1
5
1 2 3 4 5
1
5 1
"""
"""
1
4
1 2 3 4
3
1 2
3 4
2 3
"""
