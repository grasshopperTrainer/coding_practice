def solution(N):
    if N == 1:
        return '*'

    string = solution(N//3)
    l = len(string)
    end_row = [row*3 for row in string]
    middle_row = [(' '*l).join([row, row]) for row in string]
    big_string = end_row + middle_row + end_row

    return big_string


for row in solution(int(input())):
    print(row)
