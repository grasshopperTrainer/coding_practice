from sys import stdin

record = 0
for i in range(int(stdin.readline())):
    row = stdin.readline()

    param = row.strip().split(' ')
    ins = param[0]
    if ins == 'all':
        record = int('1' * 20, 2)
        continue
    elif ins == 'empty':
        record = 0
        continue

    idx = int(param[1])-1
    if ins == 'add':
        record |= 1 << idx
    elif ins == 'remove':
        record &= ~(1 << idx)
    elif ins == 'check':
        print(record >> idx & 1)
    elif ins == 'toggle':
        if record >> idx & 1:   # if there is value
            record &= ~(1 << idx)   # set 0
        else:
            record |= 1 << idx  # else set 1