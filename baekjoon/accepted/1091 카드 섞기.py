from sys import stdin


def solution(N, P, S):
    cards = tuple(range(N))

    target = {}
    for i, player in enumerate(P):
        target.setdefault(player, set()).add(i)
    if len(target) != 3:
        return -1

    visited = set()
    count = 0
    while True:
        if cards in visited:
            return -1

        # collect
        for i, c in enumerate(cards):
            if c not in target[i % 3]:
                break
        else:
            return count
        # shuffle
        visited.add(tuple(cards))
        shuffled = [0] * N
        for i, pos in enumerate(S):
            shuffled[pos] = cards[i]
        count += 1
        cards = tuple(shuffled)


N = int(stdin.readline())
P = list(map(int, stdin.readline().strip().split(' ')))
S = list(map(int, stdin.readline().strip().split(' ')))
print(solution(N, P, S))
"""
3
0 1 2
0 1 2
"""
"""
3
2 1 0
2 1 0
"""
"""
6
2 0 1 1 2 0
1 4 0 3 2 5
"""
"""
6
1 1 1 2 2 2
1 4 0 3 2 5
"""