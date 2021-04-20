from sys import stdin
from collections import deque


def solution(N, desc, X, Y):
    tree = [[] for _ in range(N + 1)]
    depth = [0 for _ in range(N + 1)]
    parents = [0 for _ in range(N + 1)]

    desc_pos =[[] for _ in range(N+1)]
    x, y = None, None

    # draw tree
    next_apple = 1
    at = [0]
    for i, c in enumerate(desc, 1):
        if c == '1':
            apple = at.pop()
            depth[apple] = len(at)  # record depth
        else:
            apple = next_apple
            parents[apple] = at[-1]
            tree[at[-1]].append(apple)
            at.append(apple)
            next_apple += 1

        # find rotten
        desc_pos[apple].append(i)
        if i in (X, Y):
            if i == X:
                x = apple
            else:
                y = apple

    # move on to lowest common ancestor
    max_depth = max(depth)
    anc_length = len(bin(max_depth-1)[2:])+1

    # fill in lca
    lca = [[0]*anc_length for _ in range(N+1)]
    que = deque([0])
    while que:
        node = que.popleft()
        for i in range(len(lca[node])):
            if i == 0:
                continue
            lca[node][i] = lca[lca[node][i-1]][i-1]

        for child in tree[node]:
            lca[child][0] = node
            que.append(child)

    # do lca searching
    while depth[x] != depth[y]:
        if depth[x] < depth[y]:
            y = parents[y]
        else:
            x = parents[x]
    if x != y:
        while parents[x] != parents[y]:
            anc_idx = 0
            while lca[x][anc_idx+1] != lca[y][anc_idx+1]:
                anc_idx += 1
            x, y = lca[x][anc_idx], lca[y][anc_idx]
        x = parents[x]
    print(' '.join(map(str, desc_pos[x])))


N = int(stdin.readline())
desc = stdin.readline().strip()
X, Y = list(map(int, stdin.readline().strip().split(' ')))

solution(N, desc, X, Y)
