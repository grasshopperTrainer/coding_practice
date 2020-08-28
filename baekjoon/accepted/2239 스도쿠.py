from sys import stdin


def solution(board):
    nums_sets = [{i: 0b111_111_111 for i in range(9)} for _ in range(3)]

    def mark(x, y, v):
        for num_set, idx in zip(nums_sets, (x // 3 + y // 3 * 3, x, y)):
            num_set[idx] ^= 1 << (v - 1)
        board[x][y] = v

    def unmark(x, y, v):
        for num_set, idx in zip(nums_sets, (x // 3 + y // 3 * 3, x, y)):
            num_set[idx] |= 1 << (v - 1)
        board[x][y] = 0

    def get_candidate(x, y):
        return nums_sets[0][x // 3 + y // 3 * 3] & nums_sets[1][x] & nums_sets[2][y]

    que = []
    for x in range(9):
        for y in range(9):
            v = board[x][y]
            if v:
                mark(x, y, v)
            else:
                que.append((x, y))
    # this yields incorrect answer as question requires answer to be min number if aligned
    # que.sort(key=lambda c: bin(get_candidate(c[0], c[1])).count('1'))

    LQ = len(que)
    def solve(que_idx):
        if que_idx == LQ:  # all filled
            return True
        x, y = que[que_idx]
        cnd = get_candidate(x, y)
        if not cnd:  # no possible number means past selection is wrong
            return False
        for shift in range(9):
            if cnd & (1 << shift):  # if the number is markable
                mark(x, y, shift + 1)
                if solve(que_idx + 1):
                    return True
                unmark(x, y, shift + 1)
        return False  # all candidate gone through but no matching means worng past

    solve(0)
    return board


board = [[int(c) for c in row.strip()] for row in stdin.readlines()]
for row in solution(board):
    print(''.join([str(i) for i in row]))

# board = '''103000509
# 002109400
# 000704000
# 300502006
# 060000050
# 700803004
# 000401000
# 009205800
# 804000107'''
# board = [[int(c) for c in row.strip()] for row in board.splitlines()]
# for row in solution(board):
#     print(' '.join([str(i) for i in row]))
"""103450000
400709123
789023056
201064089
564000231
890201504
312645000
645900012
000312045
"""
