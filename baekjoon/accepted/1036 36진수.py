from sys import stdin


CHAR_INT = {c: ord(c) - ord('A') + 10 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
for i in range(10):
    CHAR_INT[str(i)] = i
INT_CHAR = {v: k for k, v in CHAR_INT.items()}


def solution(N, nums, K):
    digits = [36 ** i for i in range(max(map(len, nums)))]

    summed = 0
    benefits = {}
    for n in nums:
        tens = 0
        for i in range(len(n)):
            c = n[len(n) - i - 1]
            v = CHAR_INT[c] * digits[i]
            summed += v
            benefits[c] = benefits.get(c, 0) + (CHAR_INT['Z'] - CHAR_INT[c]) * digits[i]
            tens += v

    benefits = sorted(benefits.items(), key=lambda x: x[1], reverse=True)

    for k in range(min(K, len(benefits))):
        summed += benefits[k][1]
    return encode(summed)


def encode(v):
    encoded = []
    while True:
        v, b = divmod(v, 36)
        encoded.append(INT_CHAR[b])
        if v == 0:
            break
    return ''.join(reversed(encoded))


N = int(stdin.readline())
nums = [stdin.readline().strip() for _ in range(N)]
K = int(stdin.readline())

print(solution(N, nums, K))
