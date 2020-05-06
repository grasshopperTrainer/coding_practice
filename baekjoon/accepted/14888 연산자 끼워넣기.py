# try recursively to avoid duplicate sings
from sys import stdin
from itertools import permutations


def solution(N, sequence, sign_count):
    ADD, SUB, MUL, DIV = 0, 1, 2, 3

    sign_seq = []
    for sign, count in zip((ADD, SUB, MUL, DIV), sign_count):
        sign_seq += [sign] * count
    first_num = sequence[0]
    sequence = sequence[1:]
    small, big = 1000000000, -1000000000
    used_order = set()
    for signs in permutations(sign_seq):
        if signs in used_order:
            continue
        used_order.add(signs)

        calced = first_num
        for n, sign in zip(sequence, signs):
            if sign == ADD:
                calced += n
            elif sign == SUB:
                calced -= n
            elif sign == MUL:
                calced *= n
            else:  # div
                mark = 1 if calced >= 0 else -1
                calced = abs(calced) // n * mark

        big = max([big, calced])
        small = min([small, calced])

    return f'{big}\n{small}'


N, sequence, sign_count = 0, 0, 0
for i, row in enumerate(stdin.readlines()):
    row = tuple(map(int, row.strip().split(' ')))
    if i == 0:
        N = row[0]
    elif i == 1:
        sequence = row
    else:
        sign_count = row

print(solution(N, sequence, sign_count))
