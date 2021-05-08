from sys import stdin


def solution(N, queries):

    candies = []
    for a, b, *c in queries:
        if a == 1:
            print(a, b)
        else:
            print(a, c[0])


N = int(stdin.readline())
queries = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
print(solution(N, queries))
