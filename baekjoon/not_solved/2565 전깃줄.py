from sys import stdin


def solution(N, wires):
    
    pass


N, wires = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        wires.append([int(c) for c in row.strip().split(' ')])

print(solution(N, wires))