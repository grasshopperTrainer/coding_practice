from sys import stdin


def solution(N, edges):
    START, END = 'A', '.'
    tree = {}
    for root, left, right in edges:
        tree[root] = left, right

    def search(tree, root):
        if root == END:
            return '', '', ''
        if root not in tree:
            return root, root, root

        lefts = search(tree, tree[root][0])
        rights = search(tree, tree[root][1])

        front = root + lefts[0] + rights[0]
        middle = lefts[1] + root + rights[1]
        end = lefts[2] + rights[2] + root
        return front, middle, end

    return search(tree, START)


N, edges = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        edges.append(row.strip().split(' '))

for a in solution(N, edges):
    print(a)