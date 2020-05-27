def hanoi(n, origin, station, target):
    if n == 0:
        return []
    result = hanoi(n-1, origin, target, station) + [(origin, target)]
    result += hanoi(n-1, station, origin, target)
    return result


solution = hanoi(int(input()), 1, 2, 3)

print(len(solution))
for a, b in solution:
    print(f'{a} {b}')
