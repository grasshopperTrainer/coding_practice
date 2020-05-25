
class Node:
    def __init__(self, val):
        self._val = val
        self._mother = None
        self._children = [None, None]
        self._offsprings_count = [0, 0]

    @property
    def value(self):
        return self._val

    @property
    def small_child(self):
        return self._children[0]
    @small_child.setter
    def small_child(self, node):
        if isinstance(node, Node):
            self._children[0] = node
        else:
            raise TypeError

    @property
    def big_child(self):
        return self._children[1]
    @big_child.setter
    def big_child(self, node):
        if isinstance(node, Node):
            self._children[1] = node
        else:
            raise TypeError

    @property
    def mother(self):
        return self._mother
    @property
    def root(self):
        if self._mother is None:
            return self
        return self._mother.root

    @property
    def is_leaf(self):
        if self._children[0] == [0, 0]:
            return True
        return False

    def __str__(self):
        return f'Node: {self._val}'

    def __repr__(self):
        return self.__str__()
    def rotate_left(self, root):
        root_root = root._mother
        new_root = root.big_child.smallest()
        for i, c in enumerate(new_root._mother._children):
            if c == new_root:
                new_root._mother._children[i] = None
        new_root._mother = root_root
        root._mother = new_root

    def rotate_right(self, root):
        root_root = root._mother
        new_root = root.small_child.biggest()
        for i, c in enumerate(new_root._mother._children):
            if c == new_root:
                new_root._mother._children[i] = None
        new_root._mother = root_root
        root._mother = new_root

    def push(self, node):
        if node._val == self._val:
            if self.small_child is None:
                self.small_child = node
                node._mother = self
                return self.root
            elif self.big_child is None:
                self.big_child = node
                node._mother = self
                return self.root
            elif self.small_child.num_family() > self.big_child.num_family():
                return self.big_child.push(node)
            else:
                return self.small_child.push(node)

        elif node._val < self._val:
            if self._children[0] is None:
                self._children[0] = node
                node._mother = self
                return self.root
            else:
                if self._children[1] is None or self._children[0].num_family() > self._children[1].num_family():
                    print('small heavy, balancing')
                    # push node to find minimal of biggest
                    self._children[0].push(node)
                    new_top = self._children[0].biggest()
                    # self._children[0].smallest()._mother._children[0] = None

                    # to relocate child of new top
                    # if new_top is right after root, it may be bigger of the root even if its smallest of biggers
                    mother_new_top = new_top.mother
                    for i, c in enumerate(mother_new_top._children):
                        if c == new_top:
                            mother_new_top._children[i] = None
                    # need balancing of _children[0]


                    # to find new_top's right child's correct position push it into mother
                    if new_top._children[0] != None:
                        new_top._children[0]._mother = None
                        mother_new_top.push(new_top._children[0])
                    # now detach node from tree
                    # and graft children of previous root
                    new_top.detach()
                    new_top.set_children(self._children)
                    new_top._mother = self._mother
                    # root._children[1] = new_top
                    if self._mother != None:
                        for i, c in enumerate(self._mother._children):
                            if c == self:
                                self._mother._children[i] = new_top
                    # new_top._mother = root
                    # detach previous root(self) from tree and push it to find correct position
                    self.remove_relationship()
                    new_top.push(self)
                    return new_top.root

                else:
                    return self._children[0].push(node)

        else:
            if self._children[1] is None:
                self._children[1] = node
                node._mother = self
                return self.root
            else:
                if self._children[0] is None or self._children[0].num_family() < self._children[1].num_family():
                    print('big heavy balancing', self)
                    # push node to find minimal of biggest
                    self._children[1].push(node)
                    new_top = self._children[1].smallest()

                    # to relocate child of new top
                    # if new_top is right after root, it may be bigger of the root even if its smallest of biggers
                    mother_new_top = new_top.mother
                    for i, c in enumerate(mother_new_top._children):
                        if c == new_top:
                            mother_new_top._children[i] = None
                    # to find new_top's right child's correct position push it into mother
                    if new_top._children[1] != None:
                        new_top._children[1]._mother = None
                        mother_new_top.push(new_top._children[1])
                    # now detach node from tree
                    # and graft children of previous root
                    new_top.detach()
                    new_top.set_children(self._children)
                    new_top._mother = self._mother
                    # root._children[1] = new_top
                    if self._mother != None:
                        for i, c in enumerate(self._mother._children):
                            if c == self:
                                self._mother._children[i] = new_top
                    # new_top._mother = root
                    # detach previous root(self) from tree and push it to find correct position
                    self.remove_relationship()
                    new_top.push(self)
                    return new_top.root
                else:
                    return self._children[1].push(node)

    def check_relationship(self):
        for c in self._children:
            if c is not None:
                if c._mother != self:
                    raise Exception(f"incorrect relationship detected - this:{self} child:{c} child'mother:{c._mother}")
                c.check_relationship()

    def num_family(self):
        if self.is_leaf:
            return 1

        total = 1
        for c in self._children:
            if c is not None:
                total += c.num_family()
        return total

    def set_children(self, children):
        for i, c in enumerate(children):
            if c is not None:
                self._children[i] = c
                c._mother = self

    def remove_relationship(self):
        self._mother = None
        for c in self._children:
            if c is not None:
                if c._mother == self:
                    c._mother = None
        self._children = [None, None]

    def smallest(self):
        if self._children[0] is None:
            return self
        return self._children[0].smallest()
    def biggest(self):
        if self._children[1] is None:
            return self
        return self._children[1].biggest()

    def inorder_traversal(self):
        if self.is_leaf:
            return [self]

        left, middle, right = [], [self], []
        if self._children[0] is not None:
            left = self._children[0].inorder_traversal()
        if self._children[1] is not None:
            right = self._children[1].inorder_traversal()
        return left + middle + right

    def pretty_print(self, prefix=''):
        SIGN_SIZE = 2
        BIG_ANGLE, SMALL_ANGLE, VERTICAL, BLANK = '╭-', '╰-', '| ', '  '
        if len(prefix) >= SIGN_SIZE:
            last_sign = prefix[len(prefix) - SIGN_SIZE: len(prefix)]
        else:
            last_sign = False

        if self._children[1] is not None:
            if not last_sign:
                big_pre = BIG_ANGLE
            elif last_sign != BIG_ANGLE:
                big_pre = prefix[:-SIGN_SIZE] + VERTICAL + BIG_ANGLE
            else:
                big_pre = prefix[:-SIGN_SIZE] + BLANK + BIG_ANGLE
            self._children[1].pretty_print(prefix=big_pre)

        print(f"{prefix}{str(self._val)}")

        if self._children[0] is not None:
            if not prefix:
                small_pre = SMALL_ANGLE
            elif last_sign != SMALL_ANGLE:
                small_pre = prefix[:-SIGN_SIZE] + VERTICAL + SMALL_ANGLE
            else:
                small_pre = prefix[:-SIGN_SIZE] + BLANK + SMALL_ANGLE
            self._children[0].pretty_print(prefix=small_pre)


import random

root = Node(3)
nums = [1, 1, 10, 3, 3, 6, 0, 2, 1, 0]
# nums = [1, 5, 5, 3, 2, 8, 1, 0, 7, 8]
for n in nums:
    print(f'inserting {n}')
    root = root.push(Node(n))
    root.pretty_print()
    print()

root = Node(3)
inserted = []
for i in range(10):
    n = random.randint(0, 10)
    inserted.append(n)
    root = root.push(Node(n))
print(inserted)
root.pretty_print()

# while True:
#     root = Node(3)
#     inserted = []
#     for i in range(100):
#         n = random.randint(0, 10)
#         inserted.append(n)
#         root = root.push(Node(n))
#     prev = None
#     for i in [r.value for r in root.inorder_traversal()]:
#         if prev is None:
#             prev = i
#         else:
#             if prev <= i:
#                 prev = i
#             else:
#                 root.pretty_print()
#                 print(inserted, root, root.inorder_traversal())
#                 raise