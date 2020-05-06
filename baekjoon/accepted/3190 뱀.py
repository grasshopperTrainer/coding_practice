from sys import stdin
from collections import deque

def solution(N, apples, moves):
    CLOCKWISE, NOTURN =  'D', -1

    apples = set(map(lambda x: (x[0]-1, x[1]-1), apples))
    moves = deque(moves)
    move_t, inst = moves.popleft()
    body = deque([(0,0)])
    occupied = {(0,0)}
    heading = (0,1)
    t = 0
    while True:
        t += 1

        t_head = body[0][0]+heading[0], body[0][1]+heading[1]
        if 0 <= t_head[0] < N and 0 <= t_head[1] < N:
            if t_head in occupied:  # body hit  body stretches first so hitting tail is possible
                break
            body.appendleft(t_head)
            occupied.add(t_head)
            if t_head in apples:    # eating apple
                apples.remove(t_head)
            else:
                occupied.remove(body.pop()) # collect tail

        else:   # hitting wall
            break

        if t == move_t: # change direction
            if inst == CLOCKWISE:
                heading = heading[1], -heading[0]
            else:
                heading = -heading[1], heading[0]

            if moves:
                move_t, inst = moves.popleft()
            else:
                move_t = NOTURN

    return t

N, apples, moves = 0, [], []
K, Q = 0, 0
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
        continue
    elif i == 1:
        K = int(row)
        continue
    elif K != 0:
        apples.append(tuple(map(int,row.strip().split(' '))))
        K -= 1
        continue
    elif Q == 0:
        Q = int(row.strip())
        continue
    else:
        t, d = row.strip().split(' ')
        moves.append((int(t), d))



# case1 = 6, ((3,4),(2,5),(5,3)), ((3,'D'),(15,'L'),(17, 'D'))
print(solution(N, apples, moves))