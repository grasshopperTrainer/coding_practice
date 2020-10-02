from sys import stdin
from itertools import combinations


def solution(W, weights):
    weights.sort()
    weight_dict = [0]*(sum(weights[len(weights)-2:])+1)

    for i, j in combinations(range(len(weights)), 2):
        s = weights[i]+weights[j]
        if weight_dict[s] == 0:
            weight_dict[s] = set()
        weight_dict[s].update([i, j])

    for v in range(len(weight_dict)):
        if weight_dict[v] != 0 and weight_dict[W-v] != 0:
            if not (weight_dict[v] & weight_dict[W-v]):
                return 'YES'
    return 'NO'


lexer = lambda: [int(c) for c in stdin.readline().strip().split(' ')]
W, N = lexer()
weights = lexer()

print(solution(W, weights))

"""
9 5
1 2 4 2 5
"""
