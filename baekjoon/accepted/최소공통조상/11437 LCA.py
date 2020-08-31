# not accepted
from sys import stdin
from collections import deque


def solution(N, edges, asked):
    root = 1
    nd_tree = {}
    for a, b in edges:
        nd_tree.setdefault(a, []).append(b)
        nd_tree.setdefault(b, []).append(a)
    # find directed tree and depth
    tree = [i for i in range(N+1)]
    node_depth = [0 for _ in range(N+1)]
    max_depth = 0
    que = deque([[1,0]])
    visited = {1}
    while que:
        at, depth = que.popleft()
        max_depth = max((max_depth, depth))
        for goto in nd_tree[at]:
            if goto not in visited:
                visited.add(goto)
                tree[goto] = at
                node_depth[goto] = depth+1
                que.append((goto, depth+1))

    ancestry_d = len(bin(max_depth)[2:])+1
    lca = [[root for _ in range(ancestry_d)] for _ in range(N+1)]
    for node in range(1, N+1):
        for anc in range(ancestry_d):
            if anc == 0:
                lca[node][anc] = tree[node]
            else:
                lca[node][anc] = lca[lca[node][anc-1]][anc-1]
    # for row in lca:
    #     print(row)
    # search asked
    answers = []
    for a, b in asked:
        # print('starting at', a, b)
        while node_depth[a] != node_depth[b]:
            if node_depth[a] > node_depth[b]:
                a = tree[a]
            else:
                b = tree[b]
        # print('after matching depth', a, b)
        # if a == b:
        #     answers.append(a)
        #     continue
        while a != b:
            anc = 0
            while lca[a][anc+1] != lca[b][anc+1]:
                anc += 1
            a, b = lca[a][anc], lca[b][anc]
        # print('after jumping', a, b, anc)
        # print()
        # while a != b:
        #     a = tree[a]
        #     b = tree[b]
        answers.append(a)
    return answers


N = int(stdin.readline())
edges = []
for _ in range(N-1):
    edges.append([int(c) for c in stdin.readline().strip().split(' ')])
M = int(stdin.readline())
asked = []
for _ in range(M):
    asked.append([int(c) for c in stdin.readline().strip().split(' ')])

for a in solution(N, edges, asked):
    print(a)
def tree_builder(N):
    root = 1
    tree = [i for i in range(N)]

    pass

"""
26
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
20 15
16 15
24 16
17 16
25 24
18 17
19 18
13 21
23 21
21 22
19 26
1
26 23
"""
"""
3
2 3
1 2
1
2 3
"""
"""
33
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
10 11
11 12
12 13
13 14
14 15
15 16
16 17
1 18
18 19
19 20
20 21
21 22
22 23
23 24
24 25
25 26
26 27
27 28
28 29
29 30
30 31
31 32
32 33
1
17 32
"""