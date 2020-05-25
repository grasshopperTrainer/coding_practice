from sys import stdin
import heapq


def solution(N, nums):
    answer = []
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        k = len(heap)
        depth = 0
        while k != 1:
            depth += 1
            k //= 2
        if len(heap) == 2**(depth+1)-1:
            s, e = 2**depth-1, 2**(depth+1)-1
            answer.append(sorted(heap[s:e])[0])
        elif len(heap) == 2**(depth+1)-2:
            s, e =
        else:
            s, e = 2**(depth-1)-1, 2**depth-1
            off = 2**(depth+1) - 1 - len(heap) - 1
            sub = sorted(heap[s:e])
            print(heap, sub, off)
            # if off%2 == 0:
            #     answer.append(sub[-off+1])
            # else:
            #     answer.append(sub[])
            print(heap, off)
            # answer.append(sorted(heap[s:e])[])
    return answer



N, nums = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums.append(int(row))

for a in solution(N, nums):
    print(a)