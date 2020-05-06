from sys import stdin

def solution(N):
    cache = {}
    def find(v):
        if v > N:
            return 0
        elif v == N:
            return 1

        if v in cache:
            return cache[v]

        ways = 0
        for a in (1, 2, 3):
            ways += find(v+a)
        cache[v] = ways
        return ways

    return find(0)


ns = []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        continue
    ns.append(int(row))

for n in ns:
    print(solution(n))
