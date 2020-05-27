# think need to use dp
from sys import stdin
from collections import Counter


def solution(n):
    if n == 1:
        return 1

    def yak(num):
        if num <= 2:
            return [num]

        yaksu = []
        while num != 1:
            for i in range(2, num+1):
                if num%i == 0:
                    yaksu.append(i)
                    num = num//i
                    break
            else:
                yaksu.append(num)
                break
        return yaksu

    divisors = Counter(yak(n))
    count = 2
    for i in range(n+2,  n*2):
        k = i-n
        counter = divisors + Counter(yak(i))
        divisors_up = Counter(yak(k))
        count += int(counter & divisors_up == divisors_up)
    return count

for row in stdin.readlines():
    print(solution(int(row.strip().split('/')[1])))