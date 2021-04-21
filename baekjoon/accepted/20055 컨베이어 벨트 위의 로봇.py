from sys import stdin
from collections import deque


class Place:
    half_len = None
    num_broken = 0
    convoyer = deque()

    def __init__(self, id, dur):
        self.id = id
        self.__dur = dur

        if self.convoyer:
            self.convoyer[-1].__next = self
            self.__next = self.convoyer[0]
        self.convoyer.append(self)

        self.robot = None

    def __str__(self):
        return f"<Place {self.id, self.__dur, bool(self.robot)}>"

    def __repr__(self):
        return self.__str__()

    @property
    def next(self):
        return self.__next

    @property
    def dur(self):
        return self.__dur

    @dur.setter
    def dur(self, v):
        self.__dur = v
        if self.__dur == 0:
            self.__class__.num_broken += 1
            self.robot = None

    @classmethod
    def move_ahead(cls):
        cls.convoyer.appendleft(cls.convoyer.pop())

    def is_dropping(self):
        return bool(self == self.convoyer[self.half_len- 1])

    def drop(self):
        self.robot.place = None
        self.robot = None


class Robot:
    def __init__(self, place):
        self.place = place

    def __str__(self):
        return f"<Robot {self.place}>"

    def __repr__(self):
        return self.__str__()

    def move_ahead(self):
        if self.place.next.dur and self.place.next.robot is None:
            self.place.robot = None
            self.place.next.dur -= 1
            self.place.next.robot = self
            self.place = self.place.next


def solution(N, K, durabilities):
    Place.half_len = N

    robots = []
    for i, j in enumerate(durabilities, 1):
        Place(i, j)

    turn = 0
    while Place.num_broken < K:
        turn += 1
        # 1
        Place.move_ahead()

        # 2
        new_robots = []
        for r in robots:
            if r.place.is_dropping():
                r.place.drop()
            else:
                r.move_ahead()
                if r.place.is_dropping():  # dropping place
                    r.place.drop()
                else:
                    new_robots.append(r)

        robots = new_robots

        # 3
        picking = Place.convoyer[0]
        if picking.dur and picking.robot is None:
            picking.dur -= 1
            robot = Robot(picking)
            picking.robot = robot
            robots.append(robot)
        # print(list(Place.convoyer)[:N])
        # print(list(reversed(list(Place.convoyer)[N:])))
        # print()
        # 4
        if K <= Place.num_broken:
            return turn


N, K = list(map(int, stdin.readline().strip().split(' ')))
durabilities = list(map(int, stdin.readline().strip().split(' ')))
print(solution(N, K, durabilities))

"""
2 4
1 1 1 1
"""