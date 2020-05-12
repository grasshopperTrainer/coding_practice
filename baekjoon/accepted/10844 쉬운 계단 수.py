def solution(N):
    record = [0]*10
    for i in range(1, 10):
        record[i] = 1

    for _ in range(1, N):
        new_record = [0]*10
        for i in range(10):
            if i != 0:
                new_record[i] += record[i-1]
            if i != 9:
                new_record[i] += record[i+1]
        record = new_record

    return sum(record)%1_000_000_000


print(solution(int(input())))