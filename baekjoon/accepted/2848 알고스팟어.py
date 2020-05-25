from sys import stdin
from collections import OrderedDict
from collections import deque, Counter


def solution(N, words):
    STRANGE, UNDEFINED = '!', '?'

    # build trie
    char_set = set()
    tree = OrderedDict()
    for word in words:
        root = tree
        for char in word:
            char_set.add(char)
            root = root.setdefault(char, OrderedDict())
        # !KILLER CASE! even if statement says words are given in correct dic order, it's not
        # root not empty means a word shorter is given after the longer, meaning it's not in dic order
        if len(root) != 0:
            return STRANGE

    BIGGER, SMALLER, UNKNOWN = -1, 1, 0
    # board for recording relationship
    board = {char: {c: UNKNOWN for c in char_set if c != char} for char in char_set}

    # find hints
    que = deque([tree])
    while que:
        t = que.pop()
        keys = list(t.keys())   # using OrderedDict to easily find relationship
        for i, (key, branch) in enumerate(t.items()):
            for smaller in keys[i+1:]:
                # need bi-directional search so record both small and big
                if board[key][smaller] in (BIGGER, UNKNOWN):
                    board[key][smaller] = BIGGER
                else:
                    return STRANGE
                if board[smaller][key] in (SMALLER, UNKNOWN):
                    board[smaller][key] = SMALLER
                else:
                    return STRANGE
            que.append(branch)

    # initiate relationship search
    que = deque()
    for origin, v in board.items():
        for k, v in board[origin].items():
            if v != UNKNOWN:    # including both BIGGER and SMALLER means gonna search bi-directional
                que.append((origin, k, v))
    # update relationship
    while que:
        origin, alpha, target = que.popleft()
        for k, v in board[alpha].items():
            # if alpha origin is bigger than alpha find smaller than alpha and mark it smaller than origin
            if v == target:
                if board[origin][k] not in (UNKNOWN, target):
                    return STRANGE
                board[origin][k] = target
                # not needed as we are searching through all alphas
                # if board[k][origin] not in (UNKNOWN, -target):
                #     return STRANGE
                # board[k][origin] = -target
                que.append((origin, k, target))

    # check undefinable
    result = {}
    for k, v in board.items():
        count = Counter(v.values())
        # using SMALLER not to reverse?
        if UNKNOWN in count or count[SMALLER] in result:
            return UNDEFINED
        result[count[SMALLER]] = k

    in_order = sorted(result.items(), key=lambda x: x[0])
    return ''.join(list(map(lambda x: x[1], in_order)))


N, words = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        words.append(row.strip())

print(solution(N, words))