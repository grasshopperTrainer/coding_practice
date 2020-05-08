from sys import stdin, setrecursionlimit

def solution(N, node_info):
    setrecursionlimit(200_000)
    class Node:
        def __init__(self, id):
            self.id = id
            self.related = []

        def add_related(self, child):
            self.related.append(child)

        def set_parent(self, root=None):
            if root is None:
                self.parent = self
            else:
                self.parent = root

            for r in self.related:
                if r != root:
                    r.set_parent(self)

    nodes = {}
    for this, that in node_info:
        a = nodes.setdefault(this, Node(this))
        b = nodes.setdefault(that, Node(that))
        a.add_related(b)
        b.add_related(a)

    nodes[1].set_parent()
    parents = [nodes[n].parent.id for n in range(2, N+1)]
    return parents

N, nodes = 0, []
for i,row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nodes.append([int(c) for c in row.strip().split(' ')])

for a in solution(N, nodes):
    print(a)