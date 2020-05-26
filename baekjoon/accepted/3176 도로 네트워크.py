# accepted! but only in PyPy3. Need optimization to avoid Python3 time over.
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
    lca_min = [[inf]*max_num_ancestors for _ in range(1, N+2)]
    lca_max = [[-inf]*max_num_ancestors for _ in range(1, N+2)]
    node_depth = {root: 0}
    # find node depth and record lca ancestors
    visited, que = {root}, deque([(root, 0)])
    while que:
        node, depth = que.popleft()
        for next_node, cost in tree[node].items():
            if next_node not in visited:
                visited.add(next_node)
                que.append((next_node, depth+1))

                # record depth
                node_depth[next_node] = depth + 1
                # record 2**0 ancestor and min_max
                lca[next_node][0] = node
                lca_min[next_node][0] = tree[next_node][node]
                lca_max[next_node][0] = tree[next_node][node]

                num_ancestors = len(bin(depth+1)[2:])
                for i in range(1, num_ancestors):   # record 2**n th ancestors
                    lca[next_node][i] = lca[lca[next_node][i-1]][i-1]
                    lca_min[next_node][i] = min([lca_min[next_node][i-1], lca_min[lca[next_node][i-1]][i-1]])
                    lca_max[next_node][i] = max([lca_max[next_node][i-1], lca_max[lca[next_node][i-1]][i-1]])

    # for i, row in enumerate(lca_min, 0):
    #     print(i, row)
    # print()
    # find lca
    answers = []
    for a, b in travels:
        min_max = [inf, -inf]
        answers.append(min_max)
        # match depth
        while node_depth[a] != node_depth[b]:
            depth_diff = abs(node_depth[a] - node_depth[b])
            anc_idx = len(bin(depth_diff)[2:]) - 1
            if node_depth[a] > node_depth[b]:
                a, mi, ma = lca[a][anc_idx], lca_min[a][anc_idx], lca_max[a][anc_idx]
            else:
                b, mi, ma = lca[b][anc_idx], lca_min[b][anc_idx], lca_max[b][anc_idx]
            min_max[:] = min([min_max[0], mi]), max([min_max[1], ma])
            # print('matching depth', a, b, min_max)

        # march toward root to find lca
        while a != b:
            if lca[a][0] == lca[b][0]:
                min_max[:] = min([min_max[0], lca_min[a][0], lca_min[b][0]]), max([min_max[1], lca_max[a][0], lca_max[b][0]])
                break

            for i, (anc_a, anc_b) in enumerate(zip(lca[a], lca[b])):
                if anc_a == anc_b:
                    min_max[0] = min([min_max[0], lca_min[a][i-1], lca_min[b][i-1]])
                    min_max[1] = max([min_max[1], lca_max[a][i-1], lca_max[b][i-1]])
                    a, b = lca[a][i-1], lca[b][i-1]
                    break
            # print('marching', a,b, min_max)
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

"""
5
2 3 100
4 3 200
1 5 150
1 3 50
1
4 5
"""
"""
12
2 3 100
4 3 200
1 5 150
1 3 50
5 9 10
5 8 200
4 6 200
6 10 100
6 11 200
4 7 30
7 12 50
7
2 9
2 8
5 12
10 2
11 10
6 4
1 10
"""
"""
13
1 2 10
1 3 10
2 4 20
3 5 20
4 6 30
6 8 40
8 10 50
10 12 60
5 7 30
7 9 40
9 11 50
11 13 60
1
12 13
"""