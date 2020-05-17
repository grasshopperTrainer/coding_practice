from sys import stdin, setrecursionlimit


def solution(pre):
    setrecursionlimit(20_000)
    def pre_to_post(pre):
        if not pre:
            return []
        elif len(pre) == 1:
            return pre

        root = pre.pop(0)
        for i, e in enumerate(pre):
            if e > root:
                if i == 0:
                    # no left, all right
                    left, right = [], pre
                else:
                    left, right = pre[:i], pre[i:]
                break
        else:
            # all left, no right
            left, right = pre, []
        return pre_to_post(left) + pre_to_post(right) + [root]

    return pre_to_post(pre)


pre_traversal = [int(l) for l in stdin.readlines()]

for a in solution(pre_traversal):
    print(a)