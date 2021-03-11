# not accepted

from sys import stdin


def solution(N, scores, idx_board, ME):
    def play(night_count, playing):
        # 2 exit conditions
        if len(playing) == 1:  # im a lone survivor
            return night_count

        longest_round = 0
        if len(playing) % 2 == 1:  # citizen's turn
            _, to_kill = sorted((scores[p], -p) for p in playing)[-1]
            to_kill = -to_kill
            if to_kill == ME:  # im to inevitably die
                return night_count
            else:
                playing.remove(to_kill)
                longest_round = play(night_count, playing)
                playing.add(to_kill)
        else:  # mafia kills
            for p in playing.copy():  # <- no copy: vary bad mistake
                if p != ME:  # is a survivor
                    kill_update(p, scores, idx_board, playing)
                    longest_round = max(longest_round, play(night_count + 1, playing))
                    resurrect_update(p, scores, idx_board, playing)
        return longest_round

    return play(0, set(range(N)))


def kill_update(p, scores, idx_board, playing):
    playing.remove(p)
    for player in playing:
        scores[player] += idx_board[p][player]


def resurrect_update(p, scores, idx_board, playing):
    for player in playing:
        scores[player] -= idx_board[p][player]
    playing.add(p)


N = int(stdin.readline())
scores = list(map(int, stdin.readline().strip().split(' ')))
board = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
me = int(stdin.readline())
print(solution(N, scores, board, me))

"""
4
500 500 500 500
1 4 3 -2
-2 1 4 3
3 -2 1 4
4 3 -2 1
2
"""

"""
2
500 300 
1 0
0 1
0
"""
"""
4
500 300 100 12
1 0 10 1
0 1 10 5
10 10 1 6
4 -1 1 1
2
"""
