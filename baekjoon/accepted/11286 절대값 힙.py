from sys import stdin


def solution(N, nums):
    def _val(heap, idx):
        return heap[idx -1]

    def _swap(heap, idx1, idx2):
        heap[idx1-1], heap[idx2-1] = heap[idx2-1], heap[idx1-1]

    def push(heap, v):
        heap.append((abs(v), v))
        idx = len(heap)
        while idx > 1:
            current_abs, current_v = _val(heap, idx)
            upper_abs, upper_v = _val(heap, idx//2)
            if upper_abs > current_abs or (upper_abs == current_abs and upper_v > current_v):
                _swap(heap, idx//2, idx)
                idx = idx//2
            else:
                break

    def pop(heap):
        if len(heap) == 0:
            raise
        elif len(heap) == 1:
            return heap.pop()[1]

        top, heap[0] = heap[0][1], heap.pop()
        idx = 1
        while True:
            children = []
            left_idx, right_idx = idx*2, idx*2+1
            if left_idx <= len(heap):
                children.append((_val(heap, left_idx), left_idx))
            if right_idx <= len(heap):
                children.append((_val(heap, right_idx), right_idx))

            if not children:
                break

            if len(children) == 2 and children[0][0][0] == children[1][0][0]:
                (lower_abs, lower_v), lower_idx = sorted(children, key=lambda x: x[0][1])[0]
            else:
                (lower_abs, lower_v), lower_idx = sorted(children, key=lambda x: x[0][0])[0]
            current_abs, current_v = _val(heap, idx)
            if lower_abs < current_abs or (lower_abs == current_abs and lower_v < current_v):
                _swap(heap, lower_idx, idx)
                idx = lower_idx
            else:
                break
        return top

    heap = []
    answer = []
    for n in nums:
        if n == 0:
            if not heap:
                answer.append(0)
            else:
                answer.append(pop(heap))
        else:
            push(heap, n)
    return answer


N, nums = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums.append(int(row))

for a in solution(N, nums):
    print(a)