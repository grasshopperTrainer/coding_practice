from math import sqrt

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue

        for j in range(2, int(sqrt(i)+1)):
            if i%j == 0 and i//j <= 10_000_000:
                answer.append(i//j)
                break
        else:
            answer.append(1)

    return answer

def numberBlock(begin, end):

    answer = [1 for i in range(end-begin+1)]

    gap =end-begin
    for i in range(2, 10000001):
        if end % i <= gap:
            for k in range(begin, end+1):
                if k%i == 0:
                    answer[k-begin] = i
    return answer

print(solution(1, 17))
print(numberBlock(1, 17))
# for i in solution(30_000_000-100, 30_000_000):
#     print(i, i> 10_000_000)