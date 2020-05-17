import random
from collections import deque


def build_binary_tree(elements):
    random.shuffle(elements)
    origin = elements.pop()
    roots = deque([origin])
    tree = {}

    while elements:
        random.shuffle(roots)
        root = roots.popleft()
        # how many children?
        children = [elements.pop() for _ in range(random.randint(0, 2)) if elements]
        if not children:
            roots.append(root)
        elif len(children) == 1:
            tree[root] = [children[0], None]
            roots.append(children[0])
        else:
            tree[root] = children
            roots.append(children[1])

    return tree, origin

def traversal(tree, root):
    if root is None:
        return [], [], []
    if root not in tree:
        return [root], [root], [root]

    lefts = traversal(tree, tree[root][0])
    rights = traversal(tree, tree[root][1])

    front = [root] + lefts[0] + rights[0]
    middle = lefts[1] + [root] + rights[1]
    end = lefts[2] + rights[2] + [root]
    return front, middle, end

origin = 1
N = 4
t, o = build_binary_tree(list(range(origin, origin+N)))
print(t, o)
print(traversal(t, o))