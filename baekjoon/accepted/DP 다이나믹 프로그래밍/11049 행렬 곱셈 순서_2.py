from sys import stdin


def solution(N, matrices):
    if N == 1:
        return matrices[0][0]*matrices[0][1]

    NORECORD = 0
    record = [[NORECORD]*N for _ in range(N)]
    def calc(s, e):
        if record[s][e] != NORECORD:
            pass
        elif s == e:
            record[s][e] = 0
        elif s+1 == e:
            record[s][e] = matrices[s][0]*matrices[s][1]*matrices[e][1]
        else:
            min_v = float('inf')
            temp = matrices[s][0]*matrices[e][1]
            for m in range(s, e):
                min_v = min((min_v, calc(s, m) + calc(m+1, e) + temp*matrices[m][1]))
            record[s][e] = min_v
        return record[s][e]

    return calc(0, N-1)


N = int(stdin.readline())
matrices = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]
print(solution(N, matrices))

"""
1
4 2
"""
"""
2
4 2
2 2
"""
"""
6
1 5
5 1
5 2
2 6
6 3
3 2
"""