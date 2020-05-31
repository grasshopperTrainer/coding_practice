# memory over
from sys import stdin

s = set()
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        continue

    param = row.strip().split(' ')
    ins = param[0]
    if ins == 'all':
        s = set([str(i) for i in range(1, 21)])
    elif ins == 'empty':
        s = set()
    elif ins == 'add':
        s.add(param[1])
    elif ins == 'remove':
        if param[1] in s:
            s.remove(param[1])
    elif ins == 'check':
        if param[1] in s:
            print(1)
        else:
            print(0)
    elif ins == 'toggle':
        if param[1] in s:
            s.remove(param[1])
        else:
            s.add(param[1])
