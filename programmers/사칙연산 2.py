
def solution(arr):
    MIN, MAX = 0, 1
    arr = tuple(arr)

    record = {}
    def dfs(arr, target):
        if (arr, target) in record:
            return record[(arr, target)]
        if len(arr) == 1:
            return int(arr[0])

        best_v = -float('inf') if target == MAX else float('inf')

        for i in range(1, len(arr), 2):
            if arr[i] == '+':
                if target == MAX:
                    best_v = max(best_v, dfs(arr[:i], MAX) + dfs(arr[i + 1:], MAX))
                else:
                    best_v = min(best_v, dfs(arr[:i], MIN) + dfs(arr[i + 1:], MAX))
            else:
                if target == MAX:
                    best_v = max(best_v, dfs(arr[:i], MAX) - dfs(arr[i + 1:], MIN))
                else:
                    best_v = min(best_v, dfs(arr[:i], MIN) - dfs(arr[i + 1:], MIN))
        record[(arr, target)] = best_v
        return best_v

    return dfs(arr, MAX)


# print(solution(["1", "-", "3", "+", "5", "-", "8"]))
# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
print(solution(
    ["5", "-", "5", "+", "5", "-", "5", "-", "5"]))
