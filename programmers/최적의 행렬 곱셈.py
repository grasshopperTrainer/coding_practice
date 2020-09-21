def solution(matrix_sizes):
    record = {}
    def dfs(s, e):
        if (s, e) in record:
            return record[(s,e)]
        if s == e:
            return 0
        if s + 1 == e:
            return matrix_sizes[s][0]*matrix_sizes[s][1]*matrix_sizes[e][1]

        min_calc = float('inf')
        for m in range(s, e):
            min_calc = min(min_calc,
                           dfs(s, m)
                           + dfs(m+1, e)
                           + matrix_sizes[s][0]*matrix_sizes[m][1]*matrix_sizes[e][1])
        record[(s,e)] = min_calc
        return min_calc
    return dfs(0, len(matrix_sizes)-1)

print(solution([[5,3],[3,10],[10,6]]))
print(solution([[5,3],[3,10],[10,6],[6,2]]))
print(solution([[5,3],[3,6],[6,10],[10,10],[10,6],[6,2]]))