def solution(G):
    answers = []
    old_weight, current_weight = 1, 1
    while True:
        weight_diff = current_weight ** 2 - old_weight ** 2

        if weight_diff < G:
            current_weight += 1
        elif G < weight_diff:
            old_weight += 1
        elif G == weight_diff:
            answers.append(current_weight)
            current_weight += 1

        if old_weight == current_weight:
            break

    return answers if answers else [-1]


for a in solution(int(input())):
    print(a)
