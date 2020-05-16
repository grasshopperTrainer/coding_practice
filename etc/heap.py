# list max heap
def _swap(heap, a, b):
    heap[a - 1], heap[b - 1] = heap[b - 1], heap[a - 1]


def _value(heap, idx):
    return heap[idx - 1]


def max_heap_push(heap, v):
    heap.append(v)
    idx = len(heap)
    while idx > 1 and _value(heap, idx // 2) < _value(heap, idx):
        _swap(heap, idx // 2, idx)
        idx = idx // 2


def min_heap_push(heap):
    if len(heap) == 0:
        raise
    elif len(heap) == 1:
        return heap.pop()

    top, heap[0] = heap[0], heap.pop()
    idx = 1
    while True:
        children = []
        if idx * 2 <= len(heap):
            children.append((_value(heap, idx * 2), idx * 2))
        if idx * 2 + 1 <= len(heap):
            children.append((_value(heap, idx * 2 + 1), idx * 2 + 1))

        if not children:
            break
        _, child_idx = sorted(children)[-1]
        if _value(heap, child_idx) > _value(heap, idx):
            _swap(heap, child_idx, idx)
            idx = child_idx
        else:
            break
    return top


# list min heap
def min_heap_push(heap, v):
    heap.append(v)
    idx = len(heap)
    while idx > 1 and _value(heap, idx // 2) > _value(heap, idx):
        _swap(heap, idx // 2, idx)
        idx = idx // 2

def min_heap_pop(heap):
    if len(heap) == 0:
        raise
    elif len(heap) == 1:
        return heap.pop()

    top, heap[0] = heap[0], heap.pop()
    idx = 1
    while True:
        children = []
        if idx * 2 <= len(heap):
            children.append((_value(heap, idx * 2), idx * 2))
        if idx * 2 + 1 <= len(heap):
            children.append((_value(heap, idx * 2 + 1), idx * 2 + 1))

        if not children:
            break
        child_val, child_idx = sorted(children)[0]
        if child_val < _value(heap, idx):
            _swap(heap, child_idx, idx)
            idx = child_idx
        else:
            break
    return top
