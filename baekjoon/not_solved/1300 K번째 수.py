from sys import stdin


def solution(N, k):
    print(N, k)
    l = 0
    num_groups = []
    for i in range(1, N+1):
        l += i
        num_groups.append(l)
    for i in range(N-1, 0, -1):
        l += i
        num_groups.append(l)

    s, e = 0, len(num_groups)-1
    while s < e:
        m = (s+e)//2
        if num_groups[m] < k:
            s = m + 1
        else:
            e = m

    print(s, e)
    print(num_groups)



# N, k = 0, 0
# for i,row in enumerate(stdin.readlines()):
#     if i == 0:
#         N = int(row)
#     else:
#         k = int(row)

print(solution(6, 8))