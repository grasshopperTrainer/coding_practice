from sys import stdin


def solution(N, K, durabilities):
    L = N * 2

    robots = []
    convoyer = [[d, False] for d in durabilities]  # durability, robot
    hopping, dropping = 0, N - 1

    turn_count = 0
    destroyed = 0
    while True:
        turn_count += 1
        # 1
        hopping, dropping = (hopping - 1) % L, (dropping - 1) % L

        # 2
        robots_alive = []
        for place in robots:
            # a) already moved at dropping position
            if place == dropping:
                convoyer[place][1] = False  # drop
                continue  # robot not alive

            # b) can move onto next
            next_place = (place + 1) % L
            if convoyer[next_place][0] and not convoyer[next_place][1]:  # can move to next
                # move robot
                convoyer[place][1], convoyer[next_place][1] = False, True
                # check destruction
                convoyer[next_place][0] -= 1
                if convoyer[next_place][0] == 0:
                    destroyed += 1

                # check if robot has to be dropped immediately
                if next_place == dropping:
                    convoyer[next_place][1] = False
                else:  # else robot alive
                    robots_alive.append(next_place)
                continue

            # c) robot can't move, stay
            robots_alive.append(place)

        robots = robots_alive

        # 3
        if convoyer[hopping][0] and not convoyer[hopping][1]:
            convoyer[hopping][1] = True
            convoyer[hopping][0] -= 1
            if convoyer[hopping][0] == 0:
                destroyed += 1
            robots.append(hopping)

        # 4
        if K <= destroyed:
            return turn_count


N, K = list(map(int, stdin.readline().strip().split(' ')))
durabilities = list(map(int, stdin.readline().strip().split(' ')))
print(solution(N, K, durabilities))

"""
2 4
1 1 1 1
"""
