
def solution(N):
    records = []
    for i in range(3):
        if i == 0:
            records.append([0]*N)
        else:
            records.append([0]*(N*2 - 1))

    def search(rn, l, taken=set()):
        if rn == l:
            return 1

        count = 0
        for cn in range(N):
            for r, k in zip(records, (cn, rn - cn, rn + cn)):
                if r[k]:
                    break
            else:
                for r, k in zip(records, (cn, rn - cn, rn + cn)):
                    r[k] = 1
                count += search(rn+1, l, taken)
                for r, k in zip(records, (cn, rn - cn, rn + cn)):
                    r[k] = 0

        return count

    return search(0, N)


print(solution(int(input())))