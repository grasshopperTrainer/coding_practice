from sys import stdin


def solution(N, costs):
    MAX = 1000*1000

    record = costs.pop(0)
    for cost in costs:
        new_record = [MAX]*3
        for i, this_cost in enumerate(cost):
            for j, prev_cost in enumerate(record):
                if i != j:
                    new_record[i] = min([new_record[i], this_cost + prev_cost])
        record = new_record

    return min(record)


N, costs = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        costs.append([int(c) for c in row.strip().split(' ')])

print(solution(N, costs))