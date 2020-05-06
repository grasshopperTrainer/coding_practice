
import sys


def solution(k, room_number):
    sys.setrecursionlimit(10000)
    d = {}
    answer = []

    def find_root(rn):
        if rn not in d:
            d[rn] = rn
            return rn
        # if d[rn] == rn:
        #     return rn

        root = find_root(d[rn])
        d[rn] = root  # important - compressing -
        return root

    for rn in room_number:
        rn = find_root(rn)
        print(d)
        d[rn] += 1
        answer.append(rn)
    return answer

print(solution(10, [1,1,1,1,2,2,2,]))