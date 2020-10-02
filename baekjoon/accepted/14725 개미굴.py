from sys import stdin


def solution(queries):
    ROOT = 'R'
    tree = {ROOT:{}}
    for query in queries:
        root = tree[ROOT]
        for c in query:
            root = root.setdefault(c, {})

    def dfs(at, root, depth):
        result = ['-'*2*depth + at]
        for k, v in sorted(root.items()):
            result += dfs(k, v, depth+1)
        return result

    return dfs(ROOT, tree['R'], -1)[1:]


queries = []
for _ in range(int(stdin.readline())):
    queries.append(stdin.readline().strip().split(' ')[1:])

for row in solution(queries):
    print(row)
