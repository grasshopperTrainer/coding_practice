from sys import stdin

DELTA = (-1, 0), (1, 0), (0, -1), (0, 1)  # up down left right


def pos_by_priority(p_rule, shark_dict, shark_id):
    x, y, d = shark_dict[shark_id]

    for p in p_rule[shark_id - 1][d - 1]:
        dx, dy = DELTA[p - 1]
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            yield nx, ny, p


def search_clean(shark_map, marking, p_rule, shark_dict, shark_id, new_moves):
    x, y, _ = shark_dict[shark_id]
    for nx, ny, new_dir in pos_by_priority(p_rule, shark_dict, shark_id):
        if (nx, ny) not in marking:  # clean
            # set
            shark_dict[shark_id] = nx, ny, new_dir
            # record move
            new_moves.setdefault((nx, ny), []).append(shark_id)
            shark_map[x][y] = 0
            return True
    return False


def search_smelly(shark_map, marking, p_rule, shark_dict, shark_id, new_moves):
    x, y, _ = shark_dict[shark_id]
    for nx, ny, new_dir in pos_by_priority(p_rule, shark_dict, shark_id):
        if marking[(nx, ny)][0] == shark_id:
            # set
            shark_dict[shark_id] = nx, ny, new_dir
            # record move
            new_moves.setdefault((nx, ny), []).append(shark_id)
            shark_map[x][y] = 0
            return


def update_new_mark(shark_map, marking, shark_dict, new_moves):
    for (x, y), sharks in new_moves.items():
        sharks.sort()

        occupier = sharks[0]
        marking[(x, y)] = occupier, k
        shark_map[x][y] = occupier

        for bitten in sharks[1:]:
            shark_dict.pop(bitten)


def update_old_mark(marking):
    new_marking = {}
    for key, (shark_id, strength) in marking.items():
        strength -= 1
        if strength != 0:
            new_marking[key] = shark_id, strength
    return new_marking


def solution(N, M, k, shark_map, shark_dir, priorities):
    # init
    shark_dict = {}
    marking = {}
    for x in range(N):
        for y in range(N):
            if shark_map[x][y]:
                shark_id = shark_map[x][y]
                shark_dict[shark_id] = x, y, shark_dir[shark_id - 1]
                marking[(x, y)] = shark_id, k  # pos, shark, strength

    # simulate per second
    for t in range(1000):
        # find shark moves
        new_moves = {}
        for shark_id in shark_dict.keys():
            if not search_clean(shark_map, marking, priorities, shark_dict, shark_id, new_moves):
                search_smelly(shark_map, marking, priorities, shark_dict, shark_id, new_moves)
        # update marking then set new mark
        marking = update_old_mark(marking)
        update_new_mark(shark_map, marking, shark_dict, new_moves)
        # exit condition
        if len(shark_dict) == 1:
            return t + 1
    return -1


parser = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, M, k = parser()
board = [parser() for _ in range(N)]
shark_dir = parser()
priorities = []
for _ in range(M):
    priorities.append([parser() for _ in range(4)])

print(solution(N, M, k, board, shark_dir, priorities))
