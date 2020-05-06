def solution(arr):
    ADD, SUB, MAX, MIN = 1, -1, 1, -1
    for i in range(len(arr)):
        if arr[i] == '+':
            arr[i] = ADD
        elif arr[i] == '-':
            arr[i] = SUB
        else:
            arr[i] = int(arr[i])
    arr = tuple(arr)

    calced = {}

    def calc(arr, sign):
        if (arr, sign) in calced:
            return calced[(arr, sign)]
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 3:
            result = arr[0] + arr[2] if arr[1] == ADD else arr[0] - arr[2]
            calced[(arr, sign)] = result
            return result

        results = []
        for i in range(1, len(arr), 2):
            left, right = arr[:i], arr[i + 1:]
            if arr[i] == ADD:
                results.append(calc(left, sign) + calc(right, sign))
            else:
                results.append(calc(left, sign * arr[i]) - calc(right, -sign * arr[i]))

        result = max(results) if sign == MAX else min(results)
        calced[(arr, sign)] = result
        return result

    return calc(arr, MAX)

print(solution(["1", "-", "3", "+", "5", "-", "8"]))