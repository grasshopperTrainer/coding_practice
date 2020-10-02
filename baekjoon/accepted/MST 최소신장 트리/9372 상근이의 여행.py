from sys import stdin


def solution(N, edges):
    board = [[0]*N for _ in range(N)]
    for a, b in map(lambda x: (x[0]-1, x[1]-1), edges):
        board[a][b] = board[b][a] = 1

    count = 0

    START = 0
    stack, visited = [goto for goto, routed in enumerate(board[START]) if routed], {START}
    while stack:
        at = stack.pop()
        if at in visited:
            continue
        visited.add(at)
        count += 1
        for goto, routed in enumerate(board[at]):
            if routed:
                stack.append(goto)

    return count


lexer = lambda :[int(c) for c in stdin.readline().strip().split(' ')]
for _ in range(int(stdin.readline())):
    N, M = lexer()
    edges = [lexer() for _ in range(M)]
    print(solution(N, edges))

