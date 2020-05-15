from sys import stdin
from math import inf, isinf
import heapq


def solution(N, origin, the_road, candidates, edges):
    tree = {}
    for s, e, l in edges:
        tree.setdefault(s, {})[e] = l
        tree.setdefault(e, {})[s] = l

    def shortest_path(n, tree, origin):
        shortest = {i: inf for i in range(1, n + 1)}
        shortest[origin] = 0
        heap = [(0, origin)]
        while heap:
            _, node = heapq.heappop(heap)
            for n_node, cost in tree.get(node, {}).items():
                if shortest[n_node] > shortest[node] + cost:
                    shortest[n_node] = shortest[node] + cost
                    heapq.heappush(heap, (shortest[n_node], n_node))
        return shortest

    from_ori = shortest_path(N, tree, origin)
    from_ends = {e: shortest_path(N, tree, e) for e in candidates}
    # !KILLER CASE!
    the_road_length = tree[the_road[0]][the_road[1]]

    correct = []
    for candidate in candidates:
        # !! path from a candidate to the one end of the road
        # doesn't necessarily mean 'the road' will be passed through.
        # 'the_road_length' is needed so to confirm the road is taken when building a path
        # min_via_crossing = min([from_ori[the_road[0]] + from_ends[candidate][the_road[0]],
        #                         from_ori[the_road[1]] + from_ends[candidate][the_road[1]]])

        min_via_crossing = min([from_ori[the_road[0]] + the_road_length + from_ends[candidate][the_road[1]],
                                from_ori[the_road[1]] + the_road_length + from_ends[candidate][the_road[0]]])

        # !KILLER CASE! infinite means unreachable so need to be checked
        if not isinf(min_via_crossing) and min_via_crossing == from_ori[candidate]:
            correct.append(candidate)

    return sorted(correct)


it = iter(stdin.readlines())
T = int(next(it))
for i in range(T):
    n, m, t, s, g, h, x, edges = 0, 0, 0, 0, 0, 0, [], []
    n, m, t = [int(c) for c in next(it).strip().split(' ')]
    s, g, h = [int(c) for c in next(it).strip().split(' ')]
    for i in range(m):
        edges.append([int(c) for c in next(it).strip().split(' ')])
    for i in range(t):
        x.append(int(next(it)))

    print(' '.join([str(i) for i in solution(n, s, [g, h], x, edges)]))

# case where there is a shortest path going through the road
# and another shortest path not going through the the road
# then the path through the road is considered an answer I guess.
"""
1
5 5 1
1 2 3
1 2 1
2 3 1
3 4 1
4 5 1
1 5 2
4
"""
