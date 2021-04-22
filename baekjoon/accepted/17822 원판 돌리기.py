from sys import stdin


def solution(N, M, T, disks, queries):
    ERASED = 0

    pointers = [0] * N
    for x, d, k in queries:
        # normalize rotation, convert clockwise to anti
        k = k % M
        if d == 0:
            k *= -1
        # rotations
        for di in range(x - 1, N, x):
            pointers[di] = (pointers[di] + k) % M

        to_erase = set()  # need to execute once after all searched
        for (di, vals), p in zip(enumerate(disks), pointers):
            for vi, v in enumerate(vals):
                if v == ERASED:
                    continue

                # check prev
                if di != 0:
                    dist = pointers[di - 1] - p
                    pvi = (vi + dist) % M
                    if disks[di - 1][pvi] == v:
                        to_erase.add((di, vi))
                        to_erase.add((di - 1, pvi))

                # check next
                if di != N - 1:
                    dist = pointers[di + 1] - p
                    nvi = (vi + dist) % M
                    if disks[di + 1][nvi] == v:
                        to_erase.add((di, vi))
                        to_erase.add((di + 1, nvi))

                # check left right
                if vals[vi - 1] == v:
                    to_erase.add((di, vi))
                    to_erase.add((di, vi - 1))
                if vals[(vi + 1) % M] == v:
                    to_erase.add((di, vi))
                    to_erase.add((di, (vi + 1) % M))
        for di, vi in to_erase:
            disks[di][vi] = ERASED
        if not to_erase:
            count = 0
            total = 0
            for disk in disks:
                for v in disk:
                    total += v
                    if v != ERASED:
                        count += 1
            if count == 0:
                return 0
            ave = total / count
            for disk in disks:
                for i, v in enumerate(disk):
                    if v == ERASED:
                        continue
                    if v < ave:
                        disk[i] += 1
                    elif ave < v:
                        disk[i] -= 1

    return sum(sum(disk) for disk in disks)


lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, M, T = lexer()
disks = [lexer() for _ in range(N)]
queries = [lexer() for _ in range(T)]

print(solution(N, M, T, disks, queries))
