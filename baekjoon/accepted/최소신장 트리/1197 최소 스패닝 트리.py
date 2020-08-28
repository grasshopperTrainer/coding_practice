from sys import stdin
import heapq


def kruscsal(V, E, edges):
    # prepare edges
    edges.sort(key=lambda x: x[2])

    ds = [i for i in range(V)]
    ds_height = [1 for _ in range(V)]
    # use disjoint set
    def ds_find(idx):
        if ds[idx] == idx:
            return idx
        # compressing
        ds[idx] = ds_find(ds[idx])
        return ds[idx]

    def ds_union(a, b):
        root_a, root_b = ds_find(a), ds_find(b)
        if root_a == root_b:
            return False
        if ds_height[root_a] < ds_height[root_b]:
            ds[root_a] = root_b
        else:
            ds[root_b] = root_a

            if ds_height[root_a] == ds_height[root_b]:
                ds_height[root_a] += 1
        return True

    cost = 0
    for a, b, w in edges:
        if ds_union(a-1, b-1):
            cost += w
    return cost

def prim(V, E, edges):
    # map vertex
    graph = {}
    for a, b, w in edges:
        graph.setdefault(a, []).append((w, b))
        graph.setdefault(b, []).append((w, a))

    # start from arbitrary 1
    selected = {1}
    heap = graph[1]
    heapq.heapify(heap)

    cost = 0
    while heap:
        w, dir = heapq.heappop(heap)
        if dir not in selected:
            selected.add(dir)
            cost += w
            for i in graph[dir]:
                heapq.heappush(heap, i)
    return cost


def solution(V, E, edges):

    if V**3 < E:
        return prim(V, E, edges)
    else:
        return kruscsal(V, E, edges)


V, E = 0, 0
edges = []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        V, E = row
    else:
        edges.append(row)
print(solution(V, E, edges))

"""
4 6
1 2 3
1 3 2
1 4 1
4 2 1
4 3 1
2 3 1
"""
"""
5 5
1 2 1
2 3 3
3 4 2
4 5 2
2 5 3
"""
"""
4 4
1 2 1
2 3 2
3 4 1
4 1 2
"""
"""
5 6
1 2 2
1 3 1
3 2 1
1 4 1
1 5 2
3 5 2
"""