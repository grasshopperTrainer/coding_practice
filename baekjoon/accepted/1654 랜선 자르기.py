from sys import stdin


def solution(K, N, cables):

    def count_segment(l):
        count = 0
        for c in cables:
            count += c//l
        return count
    s, e = 1, 2**31

    while s < e:
        m = (s+e)//2
        if count_segment(m) >= N:
            s = m + 1
        else:
            e = m - 1
    return e


K, N, cables = 0, 0, []
for i,row in enumerate(stdin.readlines()):
    if i == 0:
        K, N = [int(c) for c in row.strip().split(' ')]
    else:
        cables.append(int(row))

print(solution(K, N, cables))