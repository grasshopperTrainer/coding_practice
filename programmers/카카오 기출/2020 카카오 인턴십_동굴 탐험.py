from collections import deque


def solution(n, path, order):
    nd_graph = {}
    for a, b in path:
        nd_graph.setdefault(a, []).append(b)
        nd_graph.setdefault(b, []).append(a)

    tree = [i for i in range(n)]
    que, visited = deque([0]), {0}
    while que:
        at = que.popleft()
        for other in nd_graph[at]:
            if other not in visited:
                visited.add(other)
                tree[other] = at
                que.append(other)

    order_dict = {after: before for before, after in order}

    checked = set()
    for after, before in order_dict.items():
        if after not in checked:
            visited = set()
            que = deque([before, tree[after]])
            while que:
                at = que.popleft()
                if at == after:
                    return False
                # if at == after:
                #     return False

                if tree[at] == at:
                    # checked.update(visited)
                    continue
                if at in order_dict:
                    if order_dict[at] not in visited:
                        que.append(order_dict[at])
                        visited.add(order_dict[at])

                if tree[at] not in visited:
                    que.append(tree[at])
                    visited.add(tree[at])
    return True


print(solution(9, 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], 	[[8,5],[6,7],[4,1]] 	))
print(solution(2, [[1, 0]], [[1,0]]))
print(solution(2, [[1, 0]], [[0,1]]))
print(solution(3, [[1, 0], [0, 2]], [[2,1]]))
print(solution(3, [[1, 0], [0, 2]], [[1, 0]]))
print(solution(4, [[1, 0], [0, 2], [3,2]], [[1, 2], [2,3]]))
print(solution(6, [[0, 5], [5, 4], [1, 4], [1, 2], [2, 3]], [[4, 2], [1, 3]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
