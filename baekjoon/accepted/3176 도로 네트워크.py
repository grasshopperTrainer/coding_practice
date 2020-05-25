from sys import stdin
from math import inf
from collections import deque


def solution(N, roads, K, travels):
    # lets just set first node as root
    root = roads[0][0]
    tree = {}
    for a, b, c in roads:
        tree.setdefault(a, {})[b] = c
        tree.setdefault(b, {})[a] = c

    max_num_ancestors = len(bin(N)[2:])
    lca = [[0]*max_num_ancestors for _ in range(1, N+2)]    # 0th row is a false row
    node_depth = {root: 0}
    # find node depth and record lca ancestors
    visited, que = {root}, deque([(root, 0)])
    while que:
        node, depth = que.popleft()
        for next_node, cost in tree[node].items():
            if next_node not in visited:
                visited.add(next_node)
                que.append((next_node, depth+1))

                node_depth[next_node] = depth + 1   # record depth
                lca[next_node][0] = node            # record 2**0 ancestor
                # below is not necessary?
                num_ancestors = len(bin(depth+1)[2:])
                for i in range(1, num_ancestors):   # record 2**n th ancestors
                    lca[next_node][i] = lca[lca[next_node][i-1]][i-1]

    # need to check all road costs to common ancestors so need to go step by step?
    answers = []
    for a, b in travels:
        print('seeing', a,b)
        min_max = [inf, -inf]
        answers.append(min_max)
        # match depth
        while node_depth[a] != node_depth[b]:
            if node_depth[a] > node_depth[b]:
                a, cost = lca[a][0], tree[a][lca[a][0]]
            else:
                b, cost = lca[b][0], tree[b][lca[b][0]]
            min_max[:] = min([min_max[0], cost]), max([min_max[1], cost])
            print('pushing', a, b)


        # if common ancestor was one of a,b
        if a == b:
            continue
        # else march toward root to find lca
        while a == b:
            print('toward', a,b)
            a, cost_a = lca[a][0], tree[a][lca[a][0]]
            b, cost_b = lca[b][0], tree[b][lca[b][0]]
            min_max[:] = min([min_max[0], cost_a, cost_b]), max([min_max[1], cost_a, cost_b])
        print()
    return answers


N, roads, K, travels = 0, [], 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    elif i < N:
        roads.append([int(c) for c in row.strip().split(' ')])
    elif i == N:
        K = int(row)
    else:
        travels.append([int(c) for c in row.strip().split(' ')])

for mi, ma in solution(N, roads, K, travels):
    print(f'{mi} {ma}')
