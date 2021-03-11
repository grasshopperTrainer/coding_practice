from sys import stdin


def solution(N, M, knowing, parties):
    knowing = {k: 1 for k in knowing}
    notknowing = {}

    def mark(counter, attendants):
        for att in attendants:
            counter[att] = counter.get(att, 0) + 1

    def unmark(counter, attendents):
        for att in attendents:
            counter[att] -= 1
            if not counter[att]:
                del counter[att]

    def attend(party_i, lie_count):
        if party_i == M:
            return lie_count

        party = parties[party_i]
        if party.intersection(set(knowing)):  # someone know the truth, cant lie
            if party.intersection(set(notknowing)):  # want to tell the truth but someone was told lie
                return 0
            else:
                mark(knowing, party)
                r = attend(party_i + 1, lie_count)
                unmark(knowing, party)
                return r
        else:  # no one knows the truth
            # i lied
            mark(notknowing, party)
            i = attend(party_i + 1, lie_count + 1)
            unmark(notknowing, party)

            if party.intersection(set(notknowing)):
                j = 0
            else:
                # but i dont have to
                mark(knowing, party)
                j = attend(party_i + 1, lie_count)
                unmark(knowing, party)
            return max(i, j)

    return attend(0, 0)


lexer = lambda: [int(c) for c in stdin.readline().strip().split(' ')]
N, M = lexer()
knowing = lexer()[1:]
parties = [set(lexer()[1:]) for _ in range(M)]

print(solution(N, M, knowing, parties))

"""
3 4
0 3
1 1
2 2 1
1 2
2 4
"""

"""
3 4
1 3
1 1
1 2
2 1 2 3
1 3
"""
"""
4 3
1 1 2 3
0
0
0
"""
"""
4 4
1 1
0 1
0 2 1
0 3 4
0 2 4
"""
"""
6 5
1 6
2 4 5
2 1 2
2 2 3
2 3 4
2 5 6
"""