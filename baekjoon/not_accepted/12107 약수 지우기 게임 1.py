from sys import stdin


def solution(N):
    A, B = 1, -1

    def divisors(n):
        nums = set()
        for i in range(1, n+1):
            if n%i == 0:
                nums.add(i)
        return nums

    divisors_cache = {}
    def play(player, nums):
        if len(nums) == 1:
            return player, False

        for n in nums:
            if n in divisors_cache:
                div = divisors_cache[n]
            else:
                div = divisors(n)
                divisors_cache[n] = div
            if len(nums - div) == 1:
                return player, True

        for n in nums:
            p, result = play(-player, nums - {n})
            if result:
                return p, result

    return 'A' if play(A, set(range(1, N+1)))[0] == A else 'B'


print(solution(int(stdin.readline())))