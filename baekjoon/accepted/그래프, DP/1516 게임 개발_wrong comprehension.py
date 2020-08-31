# wrong comprehension but tried different way
from sys import stdin


def solution(N, infos):
    # use 1index
    build_time = {0: 0}
    counts = [0 for _ in range(N+1)]
    nexts = [[] for _ in range(N+1)]
    for current, info in enumerate(infos, 1):
        build_time[current] = info[0]
        for next_node in info[1:]:
            if next_node != -1:
                counts[next_node] += 1
                nexts[current].append(next_node)
    # find leaves
    leafs = []
    for i, c in enumerate(counts):
        if c == 0:
            leafs.append(i)

    total_t = 0
    # do calc
    while leafs:
        max_time = 0
        new_leafs = []
        for leaf in leafs:
            max_time = max((max_time, build_time[leaf]))
            for next_node in nexts[leaf]:
                counts[next_node] -= 1
                if not counts[next_node]:
                    new_leafs.append(next_node)
        leafs = new_leafs
        total_t += max_time
    return total_t


N = int(stdin.readline())
infos = []
for row in range(N):
    infos.append([int(c) for c in stdin.readline().strip().split(' ')])

for a in solution(N, infos):
    print(a)