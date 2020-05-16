from sys import stdin


def solution(nums):

    def _swap(heap, a, b):
        heap[a-1], heap[b-1] = heap[b-1], heap[a-1]

    def _value(heap, idx):
        return heap[idx-1]

    def heap_push(heap, v):
        heap.append(v)
        idx = len(heap)
        while idx > 1 and _value(heap, idx//2) < _value(heap, idx):
            _swap(heap, idx//2, idx)
            idx = idx//2

    def heap_pop(heap):
        if len(heap) == 0:
            raise
        elif len(heap) == 1:
            return heap.pop()

        top, heap[0] = heap[0], heap.pop()
        idx = 1
        while True:
            children = []
            if idx*2 <= len(heap):
                children.append((_value(heap, idx*2), idx*2))
            if idx*2 + 1 <= len(heap):
                children.append((_value(heap, idx*2 + 1), idx*2 + 1))

            if not children:
                break
            _, child_idx = sorted(children)[-1]
            if _value(heap, child_idx) > _value(heap, idx):
                _swap(heap, child_idx, idx)
                idx = child_idx
            else:
                break
        return top

    answers = []
    heap = []
    for n in nums:
        heap_push(heap, n)
        if n == 0:
            answers.append(heap_pop(heap))

    return answers


N, nums = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums.append(int(row))

for a in solution(nums):
    print(a)