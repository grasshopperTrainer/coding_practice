from sys import stdin
from collections import deque

MUL, DIV, PLU, SUB = '*', '/', '+', '-'
ORDER = {MUL: 1, DIV: 1, PLU: 0, SUB: 0}


def mul(a, b):
    return a * b


def div(a, b):
    i, j = divmod(a, b)
    if 0 < a:
        if j < 0:
            return i + 1
        else:
            return i
    elif j:
        return i + 1
    else:
        return i


def sub(a, b):
    return a - b


def add(a, b):
    return a + b


def calc(a, b, sign):
    if sign == MUL:
        r = mul(a, b)
    elif sign == DIV:
        r = div(a, b)
    elif sign == SUB:
        r = sub(a, b)
    else:
        r = add(a, b)
    return r


def calc_left(elements):
    a, lsign, b = (elements[i] for i in range(3))
    return calc(a, b, lsign)


def calc_right(elements):
    b, rsign, a = (elements[-i - 1] for i in range(3))
    return calc(a, b, rsign)


def replace_left(elements, r):
    for _ in range(3):
        elements.popleft()
    elements.appendleft(r)


def replace_right(elements, r):
    for _ in range(3):
        elements.pop()
    elements.append(r)


def solution(exp):
    elements = deque()
    temp = []
    for c in exp:
        if c.isnumeric():
            temp.append(c)
        else:
            if temp:
                n = int(''.join(temp))
                elements.append(n)
            temp = []
            elements.append(c)
    elements.append(int(''.join(temp)))

    if elements[0] == '-':
        elements.popleft()
        elements[0] *= -1

    while len(elements) != 1:
        lsign, rsign = elements[1], elements[-2]
        if ORDER[lsign] < ORDER[rsign]:
            r = calc_right(elements)
            replace_right(elements, r)
        elif ORDER[lsign] > ORDER[rsign]:
            r = calc_left(elements)
            replace_left(elements, r)
        else:
            lr, rr = calc_left(elements), calc_right(elements)
            if lr < rr:
                replace_right(elements, rr)
            else:
                replace_left(elements, lr)
    return elements[0]


print(solution(stdin.readline().strip()))

"""
3/-2
"""