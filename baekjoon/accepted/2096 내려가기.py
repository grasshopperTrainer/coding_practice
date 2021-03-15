from sys import stdin

N = int(stdin.readline())
row = list(map(int, stdin.readline().strip().split(' ')))
max_res, min_res = row.copy(), row.copy()
for _ in range(N-1):
    row = list(map(int, stdin.readline().strip().split(' ')))
    max_res[:] = row[0] + max(max_res[:2]), row[1] + max(max_res), row[2] + max(max_res[1:])

    min_res[:] = row[0] + min(min_res[:2]), row[1] + min(min_res), row[2] + min(min_res[1:])
print(f'{max(max_res)} {min(min_res)}')