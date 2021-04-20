from sys import stdin


def solution(a, b):
    def encode(tree, i):
        if not tree[i]:
            return '1'

        substr = []
        for child in tree[i]:
            r = encode(tree, child)
            substr.append((len(r), '0' + r))
        substr.sort()
        return ''.join(map(lambda x: x[1], substr))

    def normalize(desc):
        tree = [[] for _ in range(desc.count('0') + 1)]
        next_node = 1
        at = [0]
        for c in desc:
            if c == '0':
                tree[at[-1]].append(next_node)
                at.append(next_node)
                next_node += 1
            else:
                at.pop()

        # gonna sort children by number of descendants
        return encode(tree, 0)

    return int(normalize(a) == normalize(b))


for _ in range(int(stdin.readline())):
    a = stdin.readline().strip()
    b = stdin.readline().strip()
    print(solution(a, b))

"""
1
0010011101001011
0100011011001011
"""
