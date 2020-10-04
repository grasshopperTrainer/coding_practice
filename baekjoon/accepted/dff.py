from collections import deque
from sys import setrecursionlimit
from itertools import permutations, combinations
import random

setrecursionlimit(200100)


def solution1(n, path, order):
    tree = [i for i in range(n)]
    none_d_tree = {}
    for a, b in path:
        none_d_tree.setdefault(a, []).append(b)
        none_d_tree.setdefault(b, []).append(a)

    que = deque([0])
    visited = {0}
    while que:
        at = que.popleft()
        for n in none_d_tree[at]:
            if n not in visited:
                tree[n] = at
                que.append(n)
                visited.add(n)

    def check_loop(at, node):
        # print(at, node)
        if at == node:
            return False
        if tree[at] != at:
            return check_loop(tree[at], node)
        return True

    for before, after in order:
        # print(before, after)
        if not check_loop(before, after):
            return False
        tree[after] = before
    return True


def solution2(n, path, order):
    # draw directed tree
    none_d_tree = {}
    for a, b in path:
        none_d_tree.setdefault(a, []).append(b)
        none_d_tree.setdefault(b, []).append(a)
    tree = [i for i in range(n)]  # parent
    que = deque([0])
    visited = {0}
    while que:
        at = que.popleft()
        for node in none_d_tree[at]:
            if node not in visited:
                tree[node] = at
                que.append(node)
                visited.add(node)

    # prepare order
    before_dic = {a: b for b, a in order}

    # search for loop
    def loop_search(at):
        visited = {at}
        que = deque()
        if at in before_dic:
            que.append(before_dic[at])
        que.append(tree[at])
        while que:
            node = que.popleft()
            if node == at:
                return False
            if node not in visited:
                if node in before_dic:
                    que.append(before_dic[node])
                que.append(tree[node])
                visited.add(node)

        return visited
    checked = set()
    for i in before_dic.values():
        if i not in checked:
            # print('seeing', i)
            visited = loop_search(i)
            if visited:
                # print(i, visited)
                # checked.update(visited)
                pass
            else:
                return False
            # print('checked', checked)
    return True

print(solution2(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution2(9, 	[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], 	[[4,1],[5,2]]))
print(solution2(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
print(solution2(2, [[0, 1]], [[1, 0]]))
print(solution2(4, [[0, 1],[1,2],[2,3]], [[3, 2]]))
print(solution2(4, [[0, 3],[3,2],[1,2]], [[2, 3]]))
