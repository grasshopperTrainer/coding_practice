
def is_permutation(A, B):
    counter = {}
    for c in B:
        counter.setdefault(c, 0)
        counter[c] += 1

    for c in A:
        if c not in counter:
            return False
        counter[c] -= 1
        if not counter[c]:
            counter.pop(c)

    return True if not counter else False


print(is_permutation('tedy', 'tyde'))