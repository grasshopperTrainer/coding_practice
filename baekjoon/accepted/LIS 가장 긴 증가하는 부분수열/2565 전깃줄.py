from sys import stdin


def solution(N, wires):
    def binary_search(arr, v):
        l, r = 0, len(arr)
        while l < r:
            mid = (r+l)//2
            if arr[mid] <= v:   # 같으면 안됨 같으면 한칸 위의 것을 확인해야 하기 때문에 <=
                l, r = mid+1, r
            else:
                l, r = l, mid
        return l

    # find LIS
    series = [0] + [b for _, b in sorted(wires, key=lambda x: x[0])]
    LIS = [0]*(N+1)
    cache = [0]
    for i in range(1, N+1):
        pos = binary_search(cache, series[i])
        LIS[i] = pos
        if pos >= len(cache):
            cache.append(series[i])
        else:
            cache[pos] = series[i]
    return N-len(cache)-1


N, wires = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        wires.append([int(c) for c in row.strip().split(' ')])

print(solution(N, wires))