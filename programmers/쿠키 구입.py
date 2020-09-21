def solution(cookie):
    N = len(cookie)

    best = 0
    lsum, rsum = 0, sum(cookie)
    for m in range(N):
        lsum += cookie[m]
        rsum -= cookie[m]
        a, b = lsum, rsum
        pa, pb = 0, N-1
        while pa <= m and m+1 <= pb:
            if a == b:
                best = max(best, a)
                break
            if a < b:
                b -= cookie[pb]
                pb -= 1
            else:
                a -= cookie[pa]
                pa += 1
    return best


# print(solution([1,1,2,3]))
# print(solution([1,2,4,5]))
