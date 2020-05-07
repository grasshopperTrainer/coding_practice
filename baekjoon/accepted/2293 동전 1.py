from sys import stdin

def solution(N, K, coins):
    record = [0]*(K+1)
    record[0] = 1
    for coin in coins:
        new_record = []
        for cost, latest_case in enumerate(record):
            if cost < coin:
                new_record.append(latest_case)
            else:
                new_record.append(new_record[cost-coin] + record[cost])
        record = new_record

    return record[-1]


N, K, values = 0, 0, []
for i,row in enumerate(stdin.readlines()):
    if i == 0:
        N, K = [int(c) for c in row.strip().split(' ')]
    else:
        values.append(int(row))

print(solution(N, K, values))