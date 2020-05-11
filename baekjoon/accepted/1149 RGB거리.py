from sys import stdin

def solution(N, costs):

    pass


N, costs = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        costs.append([int(c) for c in row.strip().split(' ')])

print(solution(N, costs))