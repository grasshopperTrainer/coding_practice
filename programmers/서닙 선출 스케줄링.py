from math import ceil


def solution(n, cores):
    NC = len(cores)
    l, r = 0, max(cores)*n
    # find time and num jobs done
    while l <= r:
        lead_t = (l+r)//2
        jobs_done = sum(list(map(lambda x: lead_t//x, cores)))
        # when jobs left is less than num cores, need counting
        if jobs_done < n-NC:
            l, r = lead_t + 1, r
        else:
            l, r = l, lead_t - 1
    # check total jobs done and on, then traverse
    jobs_on = sum(list(map(lambda x: ceil(l/x), cores)))
    for i, t in enumerate(cores, 1):
        if l%t == 0:    # can allocate new job
            jobs_on += 1
            if jobs_on == n:    # last job allocated
                return i

print(solution(6, [1, 2, 3]))
# print(solution(6, [1, 2, 2, 3]))
