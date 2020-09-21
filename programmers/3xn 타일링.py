def solution(n):
    DIVISOR = 1_000_000_007
    if n%2 == 1:
        return 0
    record = [1, 3]
    if n <= 2:
        return record

    for i in range(2, n, 2):
        record = record[1], (record[1]*4-record[0]) % DIVISOR
    return record[-1]

# print(solution(4))
for i in range(0, 100, 2):
    print(solution(i))