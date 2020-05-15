from sys import stdin
from sys import setrecursionlimit

def solution(board, questions):
    setrecursionlimit(100000)

    YES, NO = 1, 0
    cache = {}
    def is_palindrome(q):
        s, e = q[0]-1, q[1]-1
        if (s,e) in cache:
            return cache[(s,e)]

        if s == e:
            cache[(s,e)] = YES
            return YES
        elif s+1 == e:
            if board[s] == board[e]:
                cache[(s,e)] = YES
            else:
                cache[(s,e)] = NO
            return cache[(s,e)]

        if board[s] != board[e]:
            cache[(s,e)] = NO
            return NO
        elif is_palindrome((s+1, e-1)):
            cache[(s,e)] = YES
            return YES

    return [is_palindrome(q) for q in questions]


board, questions = [], []
for i, row in enumerate(stdin.readlines()):
    if i in (0, 2):
        continue
    row = [int(c) for c in row.strip().split(' ')]
    if i == 1:
        board = row
    elif i > 2:
        questions.append(row)

for answer in solution(board, questions):
    print(answer)