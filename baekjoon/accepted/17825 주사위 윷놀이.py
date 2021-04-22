from sys import stdin

GRAPHS = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
          [10, 13, 16, 19],
          [20, 22, 24],
          [30, 28, 27, 26],
          [25, 30, 35]]


def is_finished(pos, graph):
    return graph == 0 and 21 <= pos


def is_occupied(horses, pos, graph):
    if is_finished(pos, graph):
        return False
    if (pos, graph) in horses:
        return True


def normalize_pos(pos, graph_idx):
    if graph_idx == 0:
        if pos in (5, 10, 15):
            new_horse = 0, {5: 1, 10: 2, 15: 3}[pos]
        elif 21 <= pos:
            new_horse = 21, 0
        else:
            new_horse = pos, 0
    elif graph_idx in (1, 2, 3):
        if pos < len(GRAPHS[graph_idx]):
            new_horse = pos, graph_idx
        else:
            pos -= len(GRAPHS[graph_idx])
            new_horse = normalize_pos(pos, 4)
    else:  # graph_idx == 4
        if pos < len(GRAPHS[4]):
            new_horse = pos, 4
        else:
            pos = 20 + pos - len(GRAPHS[4])
            new_horse = normalize_pos(pos, 0)
    return new_horse


def solution(values):
    dp = {}

    def search(horses, values, dice, score):
        normalized = [dice]
        for a, b in sorted(horses):
            normalized.append(a)
            normalized.append(b)
        normalized = tuple(normalized)
        if normalized in dp:
            return dp[normalized] + score

        if dice == len(values):
            return score

        best_score = score
        dice_val = values[dice]
        for i, (pos, graph_idx) in enumerate(horses):
            # horse is already at finished
            if is_finished(pos, graph_idx):
                continue
            # next pos
            new_pos = normalize_pos(pos + dice_val, graph_idx)
            if not is_occupied(horses, *new_pos):
                point = GRAPHS[new_pos[1]][new_pos[0]]
                horses[i] = new_pos
                best_score = max(best_score, search(horses, values, dice + 1, score + point))
                horses[i] = pos, graph_idx

        dp[normalized] = best_score - score
        return best_score

    horses = [(0, 0), (0, 0), (0, 0), (0, 0)]
    return search(horses, values, 0, 0)


print(solution(list(map(int, stdin.readline().strip().split(' ')))))
