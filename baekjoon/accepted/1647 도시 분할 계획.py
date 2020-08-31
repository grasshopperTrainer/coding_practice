from sys import stdin
import heapq


def solution(N, M, roads):
    roads.sort(key=lambda x: x[2])
    # use 1-index
    ds = [i for i in range(N+1)]
    ds_level = [0 for _ in range(N+1)]
    def root(node):
        if ds[node] == node:
            return node
        r = root(ds[node])
        ds[node] = r    # compress
        return r

    def union(a, b):
        roots = root(a), root(b)
        if roots[0] != roots[1]:
            if ds_level[roots[0]] > ds_level[roots[1]]:
                ds[roots[1]] = roots[0]
            else:
                ds[roots[0]] = roots[1]
                if ds_level[roots[0]] == ds_level[roots[1]]:
                    ds_level[roots[1]] += 1
            return True
        return False

    max_cost = 0
    costs = 0
    for a, b, c in roads:
        if union(a, b):
            costs += c
            max_cost = max(max_cost, c)
    return costs - max_cost


N, M = [int(c) for c in stdin.readline().strip().split(' ')]
roads = []
for i in range(M):
    roads.append([int(c) for c in stdin.readline().strip().split(' ')])
print(solution(N, M, roads))