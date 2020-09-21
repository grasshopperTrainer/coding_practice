# my solution
from sys import stdin, setrecursionlimit

setrecursionlimit(100_000)


def solution(V, E, from_to):
    graph = [[] for _ in range(V+1)]
    ds = [i for i in range(V+1)]
    for f, t in from_to:
        graph[f].append(t)

    checked = set()
    def dfs(at, count=0, visited={}):
        checked.add(at)
        if at not in visited:
            visited[at] = count
        else:
            for k, v in visited.items():
                if v >= visited[at]:
                    ds[k] = ds[at]
            return
        for goto in graph[at]:
            dfs(goto, count+1, visited)
        del visited[at]
        return

    for i in range(1, V+1):
        if i not in checked:
            dfs(i)
    groups = {}
    for i in range(1, V+1):
        groups.setdefault(ds[i], []).append(i)
    groups = sorted(groups.items(), key=lambda x: x[1][0])
    return [v for _, v in groups]


V, E = [int(c) for c in stdin.readline().strip().split(' ')]
from_to = []
for _ in range(E):
    from_to.append([int(c) for c in stdin.readline().strip().split(' ')])

answer = solution(V, E, from_to)
print(len(answer))
for a in answer:
    print(f"{' '.join([str(i) for i in a])} -1")


"""
5 6
1 2
2 3
3 4
4 2
4 5
5 1
"""