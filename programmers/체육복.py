def solution(n, lost, reserve):
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            reserve.remove(l + 1)
        else:
            n -= 1
    return n


# print(solution(5, [3,4], [3]))
print(solution(3, [1,2], [2,3]))
# print(solution(3, [3], [1]))
