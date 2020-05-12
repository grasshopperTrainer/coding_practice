from sys import stdin


def solution(strings):
    pass


strings = []
for row in stdin.readlines():
    strings.append(row.strip())
strings.reverse()
print(solution(strings))