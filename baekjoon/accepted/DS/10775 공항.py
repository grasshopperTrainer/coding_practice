from sys import setrecursionlimit

setrecursionlimit(100_100)


def ds_root(node, tree):
    if tree[node] == node:
        return node
    r = ds_root(tree[node], tree)
    tree[node] = r
    return r


def solution(G, P, planes):
    gates = [i for i in range(G + 1)]
    count = 0
    for gate in planes:
        gate = ds_root(gate, gates)
        if gate == 0:           # asking for None existance gate
            break
        gates[gate] = gate - 1  # redirect to previous gate
        count += 1
    return count


G = int(input())
P = int(input())
planes = []
for _ in range(P):
    planes.append(int(input()))
print(solution(G, P, planes))
