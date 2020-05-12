from sys import stdin


def solution(N, K, weight_val):
    record = [0]*(K+1)
    for item, (weight, val) in enumerate(weight_val, 1):
        new_record = []
        for bag_weight in range(K+1):
            if weight <= bag_weight:
                new_record.append(max([record[bag_weight], val]))
            else:
                new_record.append(record[bag_weight])

            if bag_weight - weight >= 0:
                new_record[-1] = max([new_record[-1], record[bag_weight - weight] + val])
        record = new_record

    return max(record)


N, K, weight_val = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, K = row
    else:
        weight_val.append(row)

print(solution(N, K, weight_val))