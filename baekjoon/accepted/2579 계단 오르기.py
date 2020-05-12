from sys import stdin


def solution(N, scores):
    # two cases
    # 1. max of 1,2 step before from 2 step before + current
    # 2. 2 step before of 1 step before + current
    record = []

    for i, score in enumerate(scores):
        record.append([score, score])
        if i-1 >= 0:
            record[i][0] = max([record[i][0], record[i-1][1] + score])
        if i-2 >= 0:
            record[i][1] = max([record[i][1], max(record[i-2]) + score])

    return max(record[-1])


N, scores = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        scores.append(int(row))

print(solution(N, scores))