from sys import stdin


def solution(consults):
    N = len(consults)
    record = [0] * (N + 1)  # to on-time finish
    for idx, (lead_t, reward) in enumerate(consults):

        if idx + lead_t < N + 1:
            passing_reward = record[idx] + reward
            for day in range(idx + lead_t, N + 1):
                if passing_reward > record[day]:
                    record[day] = passing_reward

    return max(record)


consults = []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        continue
    consults.append(tuple(map(int, row.strip().split(' '))))

print(solution(consults))
