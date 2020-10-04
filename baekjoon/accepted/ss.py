from collections import Counter


def solution(gems):
    UNIQUE_L = len(set(gems))
    L = len(gems)

    left, right = 0, 0
    temp = Counter()
    record = 0, float('inf')   # num gems, start at, end at
    while True:
        if left == L or right == L:
            break
        if len(temp) == UNIQUE_L:
            if record[1]-record[0] > right-left:
                record = left, right
                if right-left == UNIQUE_L:
                    break
            temp[gems[left]] -= 1
            if not temp[gems[left]]:
                del temp[gems[left]]
            left += 1
            continue
        # if right == L:
        #     break
        # move pointers and update temp
        if len(temp) != UNIQUE_L:
            temp[gems[right]] += 1
            right += 1

    return [record[0]+1, record[1]]