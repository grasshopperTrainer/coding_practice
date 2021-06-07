from sys import stdin
# import heapq
from collections import deque


def solution(N, M, K, supplement, trees):
    ground = [[5]*N for _ in range(N)]
    forest = [[deque() for _ in range(N)] for _ in range(N)]
    for x, y, z in trees:
        forest[x-1][y-1].append(z)

    for _ in range(K):
        num_new_trees = [[0]*N for _ in range(N)]
        num_trees = 0
        # age
        for x in range(N):
            for y in range(N):
                # forest[x][y].sort(reverse=True)
                tree_aged = deque()
                while forest[x][y] and forest[x][y][0] <= ground[x][y]:
                    tree = forest[x][y].popleft()
                    tree_aged.append(tree+1)
                    ground[x][y] -= tree
                    num_trees += 1
                    # propagate
                    if (tree + 1) % 5 == 0:
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                if (dx, dy) == (0, 0):
                                    continue
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < N and 0 <= ny < N:
                                    num_new_trees[nx][ny] += 1
                                    num_trees += 1
                # calculated nutrition from dead trees
                ground[x][y] += sum(age >> 1 for age in forest[x][y])
                # update aged trees
                forest[x][y] = tree_aged
                # supplement
                ground[x][y] += supplement[x][y]

        # not to sort, update propagation after
        for x in range(N):
            for y in range(N):
                for _ in range(num_new_trees[x][y]):
                    forest[x][y].appendleft(1)
    return num_trees


N, M, K = map(int, stdin.readline().strip().split(' '))
supplement = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
tree = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]

print(solution(N, M, K, supplement, tree))