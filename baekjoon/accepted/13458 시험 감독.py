from sys import stdin
from math import ceil

students, main, sub = None, None, None
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        continue
    elif i == 1:
        students = tuple(map(int, row.strip().split(' ')))
    else:
        main, sub = tuple(map(int, row.strip().split(' ')))

def solution(students, main, sub):
    total = sum([ceil(max([0,(student-main)])/sub)+1 for student in students])
    return total

print(solution(students, main, sub))