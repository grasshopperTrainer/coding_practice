# memory exceeded

from sys import stdin
from collections import deque


def solution(N, M, atoms, protons):
    protons = set(protons)
    protons.add(None)
    graph = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            d = abs(atoms[i] - atoms[j])
            graph[i][j] = graph[j][i] = d not in protons

    max_energy = 0
    checked = [False]*N
    for i in range(N):
        if checked[i]:
            continue
        checked[i] = True

        energy = 0
        que = deque([i])
        while que:
            at = que.popleft()
            energy += atoms[at]
            for goto, routed in enumerate(graph[at]):
                if routed and not checked[goto]:
                    que.append(goto)

        max_energy = max(max_energy, energy)

    return max_energy


N, M = map(int, stdin.readline().strip().split(' '))
atoms = [int(stdin.readline()) for _ in range(N)]
protons = [int(stdin.readline()) for _ in range(M)]

print(solution(N, M, atoms, protons))