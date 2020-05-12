from sys import stdin


def solution(N, vinos):
    if N == 1:
        return vinos[0]

    record = []
    for i, v in enumerate(vinos):
        new_record = [v, v]

        if i-1 >= 0:
            new_record[0] = v + record[-1][1]
        if i-2 >= 0:
            new_record[1] = v + max(record[-2])
        if i-3 >= 0:
            new_record[1] = max([new_record[1], v + max(record[-3])])
        record.append(new_record)

    return max([max(record[-1]), max(record[-2])])


N, vinos = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        vinos.append(int(row))

print(solution(N, vinos))