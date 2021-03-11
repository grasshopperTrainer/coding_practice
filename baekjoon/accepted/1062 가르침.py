from sys import stdin
from itertools import combinations


def solution(N, K, words):
    knowing = set('antatica')
    if K < len(knowing):
        return 0

    notknowing = set()
    alpha_sets = []
    for w in words:
        alphas = set(w).difference(knowing)
        alpha_sets.append(alphas)
        notknowing.update(alphas)

    if len(notknowing) <= K-len(knowing) or not notknowing:
        return len(words)

    max_count = 0
    for pick in combinations(notknowing, K-len(knowing)):
        pick = set(pick)
        count = 0
        for word in alpha_sets:
            if word.issubset(pick):
                count += 1
        max_count = max(max_count, count)
    return max_count


N, K = list(map(int, stdin.readline().strip().split(' ')))
words = [stdin.readline().strip() for _ in range(N)]
print(solution(N, K, words))

"""
1 5
antatica
"""
"""
1 6
antatica
"""
