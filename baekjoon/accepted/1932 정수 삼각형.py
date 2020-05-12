from sys import stdin


def solution(N, triangle):
    for i, nums in enumerate(triangle):
        if i == 0:
            continue

        for j, n in enumerate(nums):
            if j != 0:
                triangle[i][j] = max([triangle[i][j], n+triangle[i-1][j-1]])
            if j != len(nums)-1:
                triangle[i][j] = max([triangle[i][j], n+triangle[i-1][j]])

    return max(triangle[-1])


N, triangle = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        triangle.append([int(c) for c in row.strip().split(' ')])

print(solution(N, triangle))