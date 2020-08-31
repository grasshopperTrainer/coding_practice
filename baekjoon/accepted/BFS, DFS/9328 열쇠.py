from sys import stdin
from collections import deque


def solution(H, W, map, keys):
    WALL, SPACE, TREASURE = '*', '.', '$'
    DELTA = ((1, 0), (-1, 0), (0, 1), (0, -1))
    # prepare map
    map.insert(0, SPACE * W)
    map.append(SPACE * W)
    for i in range(H + 2):
        map[i] = f"{SPACE}{map[i]}{SPACE}"
    H, W = H+2, W+2

    # search tools
    doors = set()
    keys = set(keys)
    score = [0]
    visited = set()

    def bfs(at):
        que = deque([at])
        while que:
            x, y = que.popleft()
            for dx, dy in DELTA:
                nx, ny = x+dx, y+dy
                if 0 <= nx < H and 0 <= ny < W:
                    if (nx, ny) in visited:
                        continue
                    v = map[nx][ny]
                    if v == SPACE:
                        pass
                    elif v == TREASURE:
                        score[0] += 1
                    elif v == WALL:
                        visited.add((nx, ny))
                        continue
                    else:               # no space, treasure, wall
                        if v.islower(): # must be a key
                            keys.add(v)
                        else:           # must be a door
                            # if key exists, current bfs can keep searching through
                            if v.lower() in keys:
                                pass
                            else:   # else mark it as a door
                                doors.add((v.lower(), nx, ny))
                                visited.add((nx, ny))
                                continue
                    visited.add((nx, ny))
                    que.append((nx, ny))
    # search
    bfs((0,0))  # init
    while True:
        goto = None
        for door in doors:  # search for teleportable door
            if door[0] in keys:
                goto = door
                break
        if goto is None:    # nowhere to goto
            break
        bfs(goto[1:])       # teleport to the door
        doors.remove(goto)  # no need to visit the door again

    return score[0]


for _ in range(int(stdin.readline())):
    H, W = [int(c) for c in stdin.readline().strip().split(' ')]
    map = []
    for _ in range(H):
        map.append(stdin.readline().strip())
    keys = stdin.readline().strip()
    print(solution(H, W, map, keys))
