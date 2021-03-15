from sys import stdin, setrecursionlimit

setrecursionlimit(10_000)

ENDER = 'count'
COUNT = 0
trie = {}
while True:
    name = stdin.readline().strip()
    if not name:
        break
    COUNT += 1

    branch = trie
    for c in name:
        branch = branch.setdefault(c, {})
    branch[ENDER] = branch.get(ENDER, 0) + 1


def search(branch, chars):
    if ENDER in branch:
        # format percentage
        percentage = str(round(branch[ENDER] / COUNT * 100, 4))
        dec = percentage.split('.')[1]
        if len(dec) < 4:
            percentage += '0' * (4 - len(dec))

        print(f"{''.join(chars)} {percentage}")
        if len(branch) == 1:
            return

    keys = sorted(branch.keys())
    for k in keys:
        if k != ENDER:
            chars.append(k)
            search(branch[k], chars)
            chars.pop()


search(trie, [])
"""
abaab
abak
ab
"""