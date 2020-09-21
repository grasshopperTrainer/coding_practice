
def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    take0 = [0 for _ in range(len(sticker))]
    notake0 = [0 for _ in range(len(sticker))]
    take0[0], take0[1] = sticker[0], sticker[0]
    notake0[1] = sticker[1]
    for i in range(2, len(sticker)):
        s = sticker[i]
        take0[i] = max(take0[i-1], take0[i-2]+s)
        notake0[i] = max(notake0[i-1], notake0[i-2]+s)
    return max(take0[-2], notake0[-1])


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
