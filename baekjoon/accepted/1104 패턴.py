# no good

from sys import stdin


def decode(A):
    a = []
    temp = 0
    for c in A:
        if c == '0':
            temp += 1
        else:
            a.append(temp)
            temp = 0
    a.append(temp)
    return a


def solution(A, B, C):
    K = 1_000_000
    a, b = decode(A), decode(B)

    if len(a) == 1:
        if a[0] == 0:  # A:111111...
            if len(b) == 1:
                if b[0] == 0:  # B:111111....
                    return -1
                else:  # B:000000....
                    t = C // len(B)
                    c = K * (len(A) + t)
                    for i in range(1, t + 1):
                        c += len(B) * i
                    c += (len(B) * t) + (C % len(B))
                    return c
            else:  # B:0101...
                if any(C <= i for i in set(b)):  # if exists
                    return len(A) * K + B.find('0' * C)
        else:  # A:00000....
            if len(b) == 1:
                if b[0] == 0:  # B:1111111...
                    if C <= len(A) * K:
                        return 0
                    else:
                        return -1
                else:  # B:0000000...
                    return 0
            else:  # B:1001000110...
                if C <= len(A) * K:
                    return 0
                else:
                    r = C - len(A) * K
                    if C <= len(A) * K + b[0]:
                        return 0
                    elif any((r <= i for i in b)):
                        return len(A) * K + B.find('0' * r)
                    elif C <= b[-1] + len(A) * K:
                        return len(A) * K + len(B) - b[-1]

    else:  # A:10101001...
        if len(b) == 1:
            pass
        else:
            pass


A = stdin.readline().strip()
B = stdin.readline().strip()
C = int(stdin.readline())
print(solution(A, B, C))

"""
111010100001010
010000001000
6
"""
