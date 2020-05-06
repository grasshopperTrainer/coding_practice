from sys import stdin
from collections import deque


def solution(wheels, K, instructions):
    LEFT, RIGHT = 6, 2
    wheels = [deque(l) for l in wheels]

    def rotate(idx, direction, rotation):
        if idx in (-1, 4):
            return

        if direction == 1 and wheels[idx-1][RIGHT] != wheels[idx][LEFT]:
            rotate(idx + direction, direction, rotation*(-1))
            wheels[idx].rotate(rotation)
        elif direction == -1 and wheels[idx+1][LEFT] != wheels[idx][RIGHT]:
            rotate(idx + direction, direction, rotation*(-1))
            wheels[idx].rotate(rotation)

    for idx, rotation in instructions:
        idx -= 1
        rotate(idx + 1, 1, rotation*(-1))
        rotate(idx - 1, -1, rotation*(-1))
        wheels[idx].rotate(rotation)

    return sum(wheels[i][0]*(2**i) for i in range(4))


wheels, K, instructions = [], 0, []
for i, row in enumerate(stdin.readlines()):
    if i < 4:
        wheels.append([int(v) for v in row.strip()])
    elif i == 4:
        K = int(row)
    else:
        instructions.append([int(v) for v in row.strip().split(' ')])

print(solution(wheels, K, instructions))