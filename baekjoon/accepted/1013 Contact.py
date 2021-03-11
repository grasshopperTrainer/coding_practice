from sys import stdin


def solution(signal):
    if check(signal, 0, 1):
        return 'YES'
    return 'NO'


def check(signal, s, e):
    if s == len(signal):
        return True

    for i in range(e, len(signal)+1):
        subs = signal[s:i]
        if subs == '01' or (subs.startswith('10') and subs.rfind('0', 2) + 1 == subs.find('1', 2)):
            if check(signal, i, i+1):
                return True
    return False


T = int(stdin.readline())
for _ in range(T):
    print(solution(stdin.readline().strip()))

"""
1
10010111
"""
"""
1
0110001011001
"""