# not accepted
from sys import stdin
from collections import deque


def solution(N, edges, asked):
    nd_tree = {}
    for a, b in edges:
        nd_tree.setdefault(a, []).append(b)
        nd_tree.setdefault(b, []).append(a)

    answers = []
    for root, a, b in asked:
        # find directed tree and depth
        tree = [i for i in range(N+1)]
        node_depth = [0 for _ in range(N+1)]
        max_depth = 0
        que = deque([[root,0]])
        visited = {root}
        while que:
            at, depth = que.popleft()
            max_depth = max((max_depth, depth))
            for goto in nd_tree[at]:
                if goto not in visited:
                    visited.add(goto)
                    tree[goto] = at
                    node_depth[goto] = depth+1
                    que.append((goto, depth+1))
        # build ancestor table
        ancestry_d = len(bin(max_depth)[2:])+1
        lca = [[root for _ in range(ancestry_d)] for _ in range(N+1)]
        for node in range(1, N+1):
            for anc in range(ancestry_d):
                if anc == 0:
                    lca[node][anc] = tree[node]
                else:
                    lca[node][anc] = lca[lca[node][anc-1]][anc-1]
        # search asked
        while node_depth[a] != node_depth[b]:
            if node_depth[a] > node_depth[b]:
                a = tree[a]
            else:
                b = tree[b]
        while a != b:
            anc = 0
            print(a, b, anc, lca[a], lca[b], lca[a][anc+1], lca[b][anc+1])
            while lca[a][anc+1] != lca[b][anc+1]:
                anc += 1
            a, b = lca[a][anc], lca[b][anc]
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
