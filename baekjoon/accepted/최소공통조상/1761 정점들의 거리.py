from sys import stdin
from collections import deque

def farthest(node, tree):
    que, visited = deque([(node, 0)]), {node}
    while que:
        at, d = que.popleft()
        for goto in tree[at]:
            if goto not in visited:
                visited.add(goto)
                que.append((goto, d+1))
    return at, d

def middle(node, dist, tree):
    que, visited = deque([(node, 0)]), {node}
    while que:
        at, d = que.popleft()
        if d == dist:
            return at
        for goto in tree[at]:
            if goto not in visited:
                visited.add(goto)
                que.append((goto, d+1))

def solution(N, nodes, queries):
    # none directed tree
    nd_tree = {}
    for a, b, d in nodes:
        nd_tree.setdefault(a, {})[b] = d
        nd_tree.setdefault(b, {})[a] = d
    # finding optimal node?
    far_a = farthest(1, nd_tree)
    far_b = farthest(far_a[0], nd_tree)
    root = middle(far_b[0], far_b[1]//2, nd_tree)
    # directed tree
    que, visited = deque([(root, 1)]), {root}
    node_depth = [1 for _ in range(N + 1)]
    node_ordered = [root]
    d_tree = [1 for _ in range(N + 1)]
    while que:
        at, d = que.popleft()
        for k, v in nd_tree[at].items():
            if k not in visited:
                visited.add(k)
                d_tree[k] = at
                node_ordered.append(k)
                node_depth[k] = d + 1
                que.append((k, d + 1))
    # build ancestor and costs
    anc_depth = len(bin(N - 1)[2:])
    ancestors = [[(1, 0) for _ in range(anc_depth)] for _ in range(N + 1)]
    for i, node in enumerate(node_ordered, 1):
        ancestors[node][0] = d_tree[node], nd_tree[node][d_tree[node]] if node != root else 0
        for j in range(1, anc_depth):
            prev = ancestors[node][j - 1]
            anc_of_prev = ancestors[prev[0]][j - 1]
            ancestors[node][j] = anc_of_prev[0], prev[1] + anc_of_prev[1]
    # calculate route
    results = []
    for a, b in queries:
        cost = 0
        # match depth
        while node_depth[a] != node_depth[b]:
            if node_depth[a] < node_depth[b]:
                b, cost = ancestors[b][0][0], cost + ancestors[b][0][1]
            else:
                a, cost = ancestors[a][0][0], cost + ancestors[a][0][1]
        # hopping
        while a != b:
            anc = 0
            if ancestors[a][anc + 1][0] != ancestors[b][anc + 1][0]:
                anc += 1
            cost += ancestors[a][anc][1] + ancestors[b][anc][1]
            a, b = ancestors[a][anc][0], ancestors[b][anc][0]
        results.append(cost)
    return results


N = int(stdin.readline())
nodes = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N - 1)]
M = int(stdin.readline())
queries = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(M)]
for a in solution(N, nodes, queries):
    print(a)
