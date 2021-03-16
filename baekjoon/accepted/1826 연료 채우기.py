from sys import stdin


def solution(N, stations, L, P):
    pass


N = int(stdin.readline())
stations = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
L, P = map(int, stdin.readline().strip().split(' '))

print(solution(N, stations, L, P))

"""
1
1 1
15 13
"""
"""
1
1 2
5 4
10 z
"""
"""
3
4 1
5 1
8 1
10 7
"""
"""
2
5 7
12 1
10 5
"""
"""
2
2 3
4 7
14 4
"""