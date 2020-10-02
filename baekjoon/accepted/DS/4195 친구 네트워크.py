from sys import stdin


def find(node, tree):
    if node not in tree:
        tree[node] = node
    if tree[node] == node:
        return node
    tree[node] = find(tree[node], tree)
    return tree[node]


def union(a, b, tree, counter):
    roots = [find(x, tree) for x in (a, b)]
    if roots[0] == roots[1]:
        return counter[roots[0]]
    else:
        tree[roots[0]] = roots[1]
        counter[roots[1]] = counter.get(roots[1], 1) + counter.get(roots[0], 1)
        return counter[roots[1]]


def solution(relations):
    tree = {}
    counter = {}
    answers = []
    for a, b in relations:
        answers.append(union(a, b, tree, counter))
    return answers


for _ in range(int(stdin.readline())):
    F = int(stdin.readline())
    relations = [stdin.readline().strip().split(' ') for _ in range(F)]
    for a in solution(relations):
        print(a)