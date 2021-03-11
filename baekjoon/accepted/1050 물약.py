from sys import stdin
from math import inf, isinf


def solution(market, formulas):
    if 'LOVE' not in formulas:
        if 'LOVE' not in market:
            return -1
        else:
            return market['LOVE']

    min_costs = {}
    def solve(element, visited):
        if element in min_costs:
            return min_costs[element]

        min_cost = inf
        if element in market:
            min_cost = market[element]
        if element in visited:
            return min_cost
        visited.add(element)

        if element in formulas:
            for formula in formulas[element]:
                cost = 0
                for n, ele in formula:
                    cost += n * solve(ele, visited)
                min_cost = min(min_cost, cost)

        min_costs[element] = min_cost
        return min_cost

    r = solve('LOVE', set())
    if isinf(r):
        return -1
    if 1_000_000_000 < r:
        return 1_000_000_001
    else:
        return r


N, M = list(map(int, stdin.readline().strip().split(' ')))
items = {}
for _ in range(N):
    k, v = stdin.readline().strip().split(' ')
    items[k] = int(v)

formulas = {}
for _ in range(M):
    k, f = stdin.readline().strip().split('=')
    subfs = []
    for subf in f.split('+'):
        subfs.append((int(subf[0]), subf[1:]))
    formulas.setdefault(k, []).append(subfs)

print(solution(items, formulas))

"""
3 2
WATER 2
HONEY 6
HOP 9
LOVE=2WATER+4HONEY+2BEER
BEER=1CAKE+3WATER+1HOP
"""
"""
3 4
WATER 2
HONEY 6
HOP 9
LOVE=2WATER+4HONEY+2BEER
LOVE=1CAKE
BEER=1HOP+3WATER+1HOP
CAKE=1WATER+1HONEY+1BEER
"""
"""
3 0
WATER 2
HONEY 6
HOP 9
"""
"""
2 3
OIL 60
WATER 70
FIRSTPOTION=1OIL+1SECONDPOTION
SECONDPOTION=4WATER+1FIRSTPOTION
LOVE=1FIRSTPOTION+1SECONDPOTION
"""