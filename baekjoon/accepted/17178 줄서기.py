from sys import stdin
from collections import deque


def solution(N, ques):
    # normalize value
    people = []
    for que in ques:
        for i, p in enumerate(que):
            s, f = p.split('-')
            pid = str(ord(s)) + '0'*(4-len(f)) + f
            people.append(pid)
            que[i] = pid

    people.sort(reverse=True)
    waiting = deque()
    while ques:
        if not ques[0]:
            ques.popleft()
            continue

        if ques[0][0] == people[-1]:
            people.pop()
            ques[0].popleft()
        else:
            waiting.appendleft(ques[0].popleft())

        while waiting and waiting[0] == people[-1]:
            people.pop()
            waiting.popleft()
    while waiting and waiting[0] == people[-1]:
        people.pop()
        waiting.popleft()

    if waiting:
        return'BAD'
    return 'GOOD'


N = int(stdin.readline())
ques = deque([deque(stdin.readline().strip().split(' ')) for _ in range(N)])

print(solution(N, ques))