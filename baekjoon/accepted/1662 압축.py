from sys import stdin


def solution(raw):
    N = len(raw)

    def decode(i):
        count = 0
        j = i
        while j < N:
            c = raw[j]
            if c == '(':
                r, jumpto = decode(j + 1)
                count += int(raw[j-1]) * r
                count -= 1
                j = jumpto
                continue

            if c == ')':
                j = j + 1
                break
            else:
                count += 1
                j += 1
        return count, j

    return decode(0)[0]


print(solution(stdin.readline().strip()))
