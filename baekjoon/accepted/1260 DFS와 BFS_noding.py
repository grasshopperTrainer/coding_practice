# test cases correct but not accepted by BJOJ
from sys import stdin
from collections import deque
import heapq

def solution(N, M, V, routes):
    class Node:
        def __init__(self, idx):
            self.idx = idx
            self.childrend = []

        def append_child(self, child):
            heapq.heappush(self.childrend, child)

        def __lt__(self, other):
            return self.idx < other.idx

        def dfs(self, visited=set()):
            record = [self.idx]
            visited.add(self)
            for child in self.childrend:
                if child not in visited:
                    record += child.dfs(visited)
            return record

        def bfs(self):
            visited, record = {self}, []
            que = deque([self])
            while que:
                node = que.popleft()
                record.append(node.idx)
                for child in node.childrend:
                    if child not in visited:
                        visited.add(child)
                        que.append(child)
            return record

    nodes = {}
    for i in range(1, N+1):
        nodes[i] = Node(i)

    for here, there in routes:
        nodes[here].append_child(nodes[there])
        nodes[there].append_child(nodes[here])

    return nodes[V].dfs(), nodes[V].bfs()


N, M, V, routes = 0, 0, 0, []
for i,row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M, V = row
    else:
        routes.append(row)

for answer in solution(N, M, V, routes):
    print(' '.join(map(lambda x: str(x), answer)))