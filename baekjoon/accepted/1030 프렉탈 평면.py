from sys import stdin


def solution(s, N, K, R1, R2, C1, C2):
    if s == 0:
        return ['0']
    board = draw(s, N, K, 0, R1, R2, C1, C2)
    # for row in board:
    #     print(''.join(map(lambda x: str(x), row)))
    answer = ['' for _ in range(R1, R2+1)]
    for i, x in enumerate(range(R1, R2+1)):
        for y in range(C1, C2+1):
            answer[i] += str(board[x][y])
    return answer


def draw(s, N, K, color, top, bottom, left, right):
    if s == 0:
        return [[color]]
    board = [[None]*(N**s) for _ in range(N**s)]

    chunk_size = N**(s-1)
    m_idx = N//2-K//2
    for x in range(N):
        for y in range(N):
            if m_idx <= x < m_idx+K and m_idx <= y < m_idx+K:
                sub_color = 1
            else:
                sub_color = color

            sub_board = draw(s-1, N, K, sub_color, top, bottom, left, right)
            for i in range(len(sub_board)):
                for j in range(len(sub_board)):
                    board[x*chunk_size+i][y*chunk_size+j] = sub_board[i][j]
    return board


s, N, K, R1, R2, C1, C2 = map(lambda x: int(x), stdin.readline().strip().split(' '))

for row in solution(s, N, K, R1, R2, C1, C2):
    print(row)

"""
3 4 2 0 3 0 3
"""
"""
10 3 1 0 1 0 1
"""