from sys import stdin
from collections import Counter
from math import inf, isinf


def solution(sentence, words):
    L = len(sentence)
    char_words = [Counter(list(w)) for w in words]

    dp = {}

    def search(i, cost):
        if i in dp:
            return cost + dp[i]  # cost to here + cost from here
        if i == L:
            return cost

        min_cost = inf
        for w, cw in zip(words, char_words):
            if i + len(w) <= L and Counter(sentence[i:i + len(w)]) == cw:
                # calc cost
                c = 0
                for a, b in zip(w, sentence[i:i + len(w)]):
                    if a != b:
                        c += 1
                min_cost = min(min_cost, search(i + len(w), cost + c))
        dp[i] = min_cost - cost  # need best cost from here
        return min_cost

    r = search(0, 0)
    if isinf(r):
        return -1
    return r


sentence = stdin.readline().strip()
N = int(stdin.readline())
words = [stdin.readline().strip() for _ in range(N)]
print(solution(sentence, words))

"""
neotwheret
4
one
two
three
there
"""
"""
abaa
3
aa
ba
aaab
"""
