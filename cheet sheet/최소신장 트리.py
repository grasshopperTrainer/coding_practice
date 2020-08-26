"""
최소 신장 트리
2가지 알고리즘: 크루스칼, 프림
"""
# 크루스칼: !!!간선!!!의 최소 가중치를 우선으로 선택해가며 트리를 그린다.
# ex) 1197 최소 스패닝 트리
# 실상 disjoint set 의 구현이 본체다
def solution(V, E, edges):
    # prepare edges
    edges.sort(key=lambda x: x[2])

    ds = [i for i in range(V)]
    ds_height = [0 for _ in range(V)]
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
            return False    # 조인이 이루어졌는가 확인하기 위한 flag
        if ds_height[root_a] < ds_height[root_b]:
            ds[root_a] = root_b
        else:
            ds[root_b] = root_a
            # 본 else 가 같은 경우도 포함하므로
            if ds_height[root_a] == ds_height[root_b]:
                ds_height[root_a] += 1
        return True

    cost = 0
    for a, b, w in edges:
        if ds_union(a-1, b-1):
            cost += w

    return cost

# 프림: 무작위 점에서 시작하여 최소로 이동할 수 있는 다음 점을 선택해가며 트리를 그린다.
# 백준 케이스에서는 크루스칼이 프림보다 빨랐음.
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