
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
        if self._children == [0, 0]:
            return True
        return False

    def __str__(self):
        return f'Node: {self._val}'

    def __repr__(self):
        return self.__str__()

    @classmethod
    def relate(cls, mother, child, place):
        if child is None:
            if mother is None:
                pass
            else:
                mother._children[place] = None
        else:
            if mother is None:
                child._mother = None
            else:
                mother_children = mother._children[:]
                child_mother = child._mother

                mother._children[place] = child
                if mother_children[place] is not None:
                    mother_children[place]._mother = None
                child._mother = mother

                if child_mother is not None:
                    for i, c in enumerate(child_mother._children):
                        if c == child:
                            child_mother._children[i] = None

    def rotate(self, root, way):
        print('before rotateion:')
        root.pretty_print()
        print()
        if way not in ('l', 'r'):
            raise
        way = 1 if way == 'l' else 0

        new_root = root.big_child.smallest() if way == 1 else root.small_child.biggest()
        mother_root = root._mother
        children_root = root._children[:]
        mother_new_root = new_root._mother
        child_new_root = new_root._children[way]

        new_root.detach()
        root.detach()

        # relate with mother of original root
        if mother_root is not None:
            for i, c in enumerate(mother_root._children):
                if c == root:
                    self.relate(mother_root, new_root, i)
        else:
            new_root._mother = None
        # graft child of new root to mother of new_root
        if mother_new_root != root:
            for i, c in enumerate(mother_new_root._children):
                if c == new_root:
                    self.relate(mother_new_root, child_new_root, i)
        else:
            self.relate(new_root, child_new_root, way)

        if children_root[way] != new_root:
            self.relate(new_root, children_root[way], way)
        self.relate(root, children_root[not way], not way)
        self.relate(new_root, root, not way)
        for c in new_root._children:
            if c is not None:
                while True:
                    rotate = c.is_inbalanced()
                    if rotate:
                        c = self.rotate(c, rotate)
                    else:
                        break
        return new_root

    def is_inbalanced(self):
        if self._children == [None, None]:
            return False
        num_small = 0 if self.small_child is None else self.small_child.num_family()
        num_big = 0 if self.big_child is None else self.big_child.num_family()
        if num_small+1 < num_big:
            return 'l'
        elif num_small > num_big+1:
            return 'r'
        else:
            return False

    def num_offsprings(self):
        if self._children == [0,0]:
            return 1
        left, right = 0, 0
        if self.small_child is not None:
            left = sum(self.small_child.num_offsprings())
        if self.big_child is not None:
            right = sum(self.big_child.num_offsprings())
        return left, right

    def push(self, node):
        # new node going left
        if node._val < self._val:
            if self.small_child is None:
                self.small_child = node
                node._mother = self
                return self.root
            else:
                return self.small_child.push(node)
        else:
            print(self.num_offsprings())
            if self.big_child is None:
                self.big_child = node
                node._mother = self
                return self.root
            else:
                return self.big_child.push(node)

    def check_relationship(self):
        for c in self.children:
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
                self.children[i] = c
                c._mother = self

    def detach(self):
        self._mother = None
        for c in self._children:
            if c is not None:
                if c._mother == self:
                    c._mother = None
        self._children = [None, None]

    def smallest(self):
        if self.small_child is None:
            return self
        return self.small_child.smallest()
    def biggest(self):
        if self.big_child is None:
            return self
        return self.big_child.biggest()

    def inorder_traversal(self):
        if self.is_leaf:
            return [self]

        left, middle, right = [], [self], []
        if self.children[0] is not None:
            left = self.children[0].inorder_traversal()
        if self.children[1] is not None:
            right = self.children[1].inorder_traversal()
        return left + middle + right

    def pretty_print(self, prefix=''):
        SIGN_SIZE = 2
        BIG_ANGLE, SMALL_ANGLE, VERTICAL, BLANK = '╭-', '╰-', '| ', '  '
        if len(prefix) >= SIGN_SIZE:
            last_sign = prefix[len(prefix) - SIGN_SIZE: len(prefix)]
        else:
            last_sign = False

        if self.big_child is not None:
            if not last_sign:
                big_pre = BIG_ANGLE
            elif last_sign != BIG_ANGLE:
                big_pre = prefix[:-SIGN_SIZE] + VERTICAL + BIG_ANGLE
            else:
                big_pre = prefix[:-SIGN_SIZE] + BLANK + BIG_ANGLE
            self.big_child.pretty_print(prefix=big_pre)

        print(f"{prefix}{str(self._val)}")

        if self.small_child is not None:
            if not prefix:
                small_pre = SMALL_ANGLE
            elif last_sign != SMALL_ANGLE:
                small_pre = prefix[:-SIGN_SIZE] + VERTICAL + SMALL_ANGLE
            else:
                small_pre = prefix[:-SIGN_SIZE] + BLANK + SMALL_ANGLE
            self.small_child.pretty_print(prefix=small_pre)


import random

# root = Node(3)
# nums = [1, 1, 10, 3, 3, 6, 0, 2, 1, 0]
# # nums = [1, 5, 5, 3, 2, 8, 1, 0, 7, 8]
# for n in nums:
#     print(f'inserting {n}')
#     root = root.push(Node(n))
#     root.pretty_print()
#     print()

root = Node(3)
root = root.push(Node(4))
root = root.push(Node(5))
inserted = []
# for i in range(20):
#     n = random.randint(0, 100)
#     print(f'{n} inserting')
#     inserted.append(n)
#     root = root.push(Node(n))
#     root.pretty_print()
#     print()
root.pretty_print()
print(inserted)
# root.pretty_print()

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