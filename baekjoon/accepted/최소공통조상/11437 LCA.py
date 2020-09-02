from sys import stdin, setrecursionlimit


setrecursionlimit(50_100)
def solution(N, edges, asked):
    # build none directed tree
    ROOT = 1
    nd_tree = {}
    for a, b in edges:
        nd_tree.setdefault(a, []).append(b)
        nd_tree.setdefault(b, []).append(a)

    # build ancestor tree with implicit directed tree
    node_depth = [0 for _ in range(N+1)]
    ancestry_d = len(bin(50_000)[2:])
    anc = [[ROOT]*ancestry_d for _ in range(N+1)]
    def build_anc(node, ancestor):
        node_depth[node] = node_depth[ancestor] + 1 # update depth
        anc[node][0] = ancestor
        # look back anc and fill in ancestors
        for i in range(1, ancestry_d):
            anc[node][i] = anc[anc[node][i-1]][i-1]
        # continue filling in ancestors
        for child in nd_tree[node]:
            if child != ancestor:
                build_anc(child, node)
    build_anc(1, 1)

    # search asked
    answers = []
    for a, b in asked:
        # match depth
        while node_depth[a] != node_depth[b]:
            if node_depth[a] > node_depth[b]:
                a = anc[a][0]
            else:
                b = anc[b][0]
        # find lowest
        while a != b:
            ca = 0
            while anc[a][ca+1] != anc[b][ca+1]:
                ca += 1
            a, b = anc[a][ca], anc[b][ca]
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