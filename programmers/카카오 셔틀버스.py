from collections import deque


def solution(n, t, m, timetable):
    FIRST_ARRIVAL = 540

    def time_to_number(time):
        return (lambda x, y: x * 60 + y)(*[int(c) for c in time.split(':')])

    def number_to_time(num):
        return ':'.join(['0' * (1 - c // 10) + str(c) for c in divmod(num, 60)])

    crew = deque(sorted(time_to_number(t) for t in timetable))

    last_seated = None
    arival = FIRST_ARRIVAL
    for i in range(n):
        seat_left = m
        while crew and crew[0] <= arival and seat_left:
            seat_left -= 1
            last_seated = crew.popleft()

        if i == n - 1:  # last bus
            if seat_left:
                last_time = arival
            else:
                last_time = last_seated - 1

        arival += t
    return number_to_time(last_time)