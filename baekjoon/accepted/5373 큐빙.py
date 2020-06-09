# need to think of refactoring
from sys import stdin
from itertools import product
from copy import deepcopy


class Face:
    def __init__(self, color=None):
        self.data = [[color]*3 for _ in range(3)]
        self.index_map = [[(x, y) for y in range(3)] for x in range(3)]

    @classmethod
    def inherit_from(cls, face):
        ins = cls()
        ins.data = face.data
        return ins

    def rotate_ori(self, count=1):
        index_map = self.index_map
        for _ in range(count):
            new_index_map = [[None]*3 for _ in range(3)]
            for x, y in product(range(3), repeat=2):
                new_index_map[2-y][x] = index_map[x][y]
            index_map = new_index_map
        ins = self.inherit_from(self)
        ins.index_map = index_map
        return ins

    def rotate_clockwise(self):
        new_data = deepcopy(self.data)
        for x, y in product(range(3), repeat=2):
            self.data[x][y] = new_data[2-y][x]

    def rotate_anticlockwise(self):
        new_data = deepcopy(self.data)
        for x, y in product(range(3), repeat=2):
            self.data[x][y] = new_data[y][2-x]

    def get_vals(self, rows, cols):
        vals = []
        for x, y in product(rows, cols):
            x, y = self.index_map[x][y]
            vals.append(self.data[x][y])
        return vals

    def set_vals(self, rows, cols, vals):
        for (x, y), val in zip(product(rows, cols), vals):
            x, y = self.index_map[x][y]
            self.data[x][y] = val


def solution(operations):
    U, D, F, B, L, R = list('UDFBLR')
    CW, CCW = '+', '-'

    # define 6 faces
    faces = {}
    for name, color in zip(list('UDFBLR'), list('wyrogb')):
        faces[name] = Face(color)

    # set surroundings of each faces
    circle = {}
    circle[U] = [faces[B], faces[L], faces[F], faces[R]]
    circle[D] = [faces[B].rotate_ori(2), faces[R], faces[F].rotate_ori(2), faces[L]]
    circle[F] = [faces[U], faces[L].rotate_ori(1), faces[D].rotate_ori(2), faces[R].rotate_ori(3)]
    circle[B] = [faces[D].rotate_ori(2), faces[L].rotate_ori(3), faces[U], faces[R].rotate_ori(1)]
    circle[L] = [faces[B].rotate_ori(1), faces[D], faces[F].rotate_ori(3), faces[U]]
    circle[R] = [faces[B].rotate_ori(3), faces[U], faces[F].rotate_ori(1), faces[D]]

    for name, rotation in operations:
        face = faces[name]
        t, l, b, r = circle[name]
        pieces = [t.get_vals([2], range(3)),
                  l.get_vals(range(3), [2]),
                  b.get_vals([0], range(3)),
                  r.get_vals(range(3), [0])]

        if rotation == CW:
            face.rotate_clockwise()
            t.set_vals([2], range(3), reversed(pieces[1]))
            l.set_vals(range(3), [2], pieces[2])
            b.set_vals([0], range(3), reversed(pieces[3]))
            r.set_vals(range(3), [0], pieces[0])
        else:
            face.rotate_anticlockwise()
            t.set_vals([2], range(3), pieces[3])
            l.set_vals(range(3), [2], reversed(pieces[0]))
            b.set_vals([0], range(3), pieces[1])
            r.set_vals(range(3), [0], reversed(pieces[2]))

    return '\n'.join([''.join(row) for row in faces[U].data])


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    operations = [tuple(c) for c in stdin.readline().strip().split(' ')]

    print(solution(operations))

"""
1
2
F+ B+
"""
"""
1
10
L- U- L+ U- L- U- U- L+ U+ U+
"""
"""
1
4
U- D- L+ R+
"""