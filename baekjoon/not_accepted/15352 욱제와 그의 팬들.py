# memory over
from sys import stdin


def solution(K, N, fans, Q, acts):
    # !KILLER CASE! even building initial data falls into memory over
    fans = {i: [i-1, i+1,  club] for i, club in enumerate(fans, 1)}
    present = 0
    for act, pos in acts:
        if act == 1:
            l, r, _ = fans[pos]
            if l in fans:
                fans[l][1] = r
            if r in fans:
                fans[r][0] = l
            del fans[pos]
        else:
            present += 1
            l, r, group = fans[pos]
            while l > 0 and fans[l][2] == group:
                present += 1
                l = fans[l][0]
            while r < N+1 and fans[r][2] == group:
                present += 1
                r = fans[r][1]

    return present


K, N, fans, Q, acts = 0, 0, [], 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 2:
        Q = int(row)
    else:
        row = [int(c) for c in row.strip().split(' ')]
        if i == 0:
            K, N = row
        elif i == 1:
            fans = row
        else:
            acts.append(row)

print(solution(K, N, fans, Q, acts))
