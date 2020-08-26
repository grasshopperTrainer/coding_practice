from sys import stdin


def solution(N):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    S, E = 1, N
    unit = 1
    def count_chiper(num, unit):
        while num:
            counter[num%10] += unit
            num //= 10

    while True:
        # move start and end
        while S%10 != 0 and S <= E:
            count_chiper(S, unit)
            S += 1
        if S > E:
            break
        while E%10 != 9 and S <= E:
            count_chiper(E, unit)
            E -= 1
        if S > E:
            break

        S //= 10
        E //= 10
        count = E - S + 1
        for i in range(10):
            counter[i] += count*unit
        unit *= 10

    return counter


N = int(stdin.readline())
print(' '.join([str(i) for i in solution(N)]))

# def dum_solution(N):
#     counter = [0,0,0,0,0,0,0,0,0,0]
#     for i in range(1, N+1):
#         for c in str(i):
#             counter[int(c)] += 1
#     return counter
#
# print(' '.join([str(i) for i in dum_solution(N)]))
