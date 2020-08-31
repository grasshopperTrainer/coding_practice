# not accepted
from sys import stdin

def solution(N, edges, asked):
    # find directed tree and depth
    tree = [i for i in range(N+1)]
    for p, c in edges:
        tree[c] = p

    node_depth = [0 for _ in range(N+1)]
    max_depth = 0
    for i in range(1, N+1):
        depth = 0
        at = i
        while tree[at] != at:
            at = tree[at]
            depth += 1
        node_depth[i] = depth
        max_depth = max((max_depth, depth))


    ancestry_d = len(bin(max_depth)[2:])+1
    lca = [[0 for _ in range(ancestry_d)] for _ in range(N+1)]
    for node in range(1, N+1):
        for anc in range(ancestry_d):
            if anc == 0:
                lca[node][anc] = tree[node]
            else:
                lca[node][anc] = lca[lca[node][anc-1]][anc-1]
    a, b = asked
    while node_depth[a] != node_depth[b]:
        if node_depth[a] > node_depth[b]:
            a = tree[a]
        else:
            b = tree[b]
    while a != b:
        anc = 0
        while lca[a][anc+1] != lca[b][anc+1]:
            anc += 1
        a, b = lca[a][anc], lca[b][anc]
    return a


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    edges = []
    for _ in range(N-1):
        edges.append([int(c) for c in stdin.readline().strip().split(' ')])
    asked = [int(c) for c in stdin.readline().strip().split(' ')]
    print(solution(N, edges, asked))

# def tree_builder(N):
#     root = 1
#     tree = [i for i in range(N)]
#
#     pass
"""
1
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7

6 11
10 9
2 6
7 6
8 13
8 15
"""
"""
1
5
2 3
3 4
3 1
1 5
3 5
"""