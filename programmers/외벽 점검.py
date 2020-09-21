def solution(n, weak, dist):
    NW, NF = len(weak), len(dist)
    dist.sort(reverse=True)

    record = {}
    def dfs(friend, weak_left):
        if (friend, *weak_left) in record:
            return record[(friend, *weak_left)]
        if not weak_left:
            return friend
        if friend == NF:
            return float('inf')

        best = float('inf')
        coverage = dist[friend]
        for search_s in weak_left:
            search_e = search_s + coverage
            new_weak = []
            if search_e >= n:
                search_e %= n
                for weak_spot in weak_left:
                    if not (weak_spot <= search_e or search_s <= weak_spot):
                        new_weak.append(weak_spot)
            else:
                for weak_spot in weak_left:
                    if not (search_s <= weak_spot <= search_e):
                        new_weak.append(weak_spot)
            best = min(best, dfs(friend + 1, new_weak))
        record[(friend, *weak_left)] = best
        return best

    answer = dfs(0, weak)
    if answer == float('inf'):
        return -1
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 5, 6, 10], [4, 5]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
