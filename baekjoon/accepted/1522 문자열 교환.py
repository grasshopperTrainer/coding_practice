from sys import stdin


def solution(string):
    num_a = string.count('a')
    num_b = string.count('b', 0, num_a)
    best = num_b
    for i in range(-1, -len(string), -1):
        if string[i] == 'b':
            num_b += 1
        if string[num_a+i] == 'b':
            num_b -= 1
        best = min(best, num_b)
    return best


print(solution(stdin.readline().strip()))