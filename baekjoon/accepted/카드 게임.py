from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(4_000_100)


def ds_find(node, tree):
    if tree[node] == node:
        return node
    tree[node] = ds_find(tree[node], tree)
    return tree[node]


def ds_union(a, b, tree, tree_height):
    roots = [ds_find(node, tree) for node in (a, b)]
    if roots[0] == roots[1]:
        return False
    heights = [tree_height[node] for node in roots]
    if heights[0] > heights[1]:
        tree[roots[1]] = roots[0]
    else:
        tree[roots[0]] = roots[1]
        if heights[0] == heights[1]:
            tree_height[roots[1]] += 1
    return True


def solution(N, M, K, cards, draws):
    tree = [i for i in range(M)]

    answers = []
    cards.sort()
    for draw in draws:
        card_i = bisect.bisect_right(cards, draw)
        card_i = ds_find(card_i, tree)
        answers.append(cards[card_i])
        tree[card_i] += 1
    return answers


N, M, K = 0, 0, 0
cards = []
draws = []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M, K = row
    if i == 1:
        cards = row
    else:
        draws = row

for a in solution(N, M, K, cards, draws):
    print(a)

"""
10 7 5
1 2 2 3 4 5 9
1 8 2 1 2
"""