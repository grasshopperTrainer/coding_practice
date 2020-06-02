from sys import stdin

def solution(N, curves):
    def rotate_clockwise(anchor, point):
        dx, dy = map(lambda x,y: x-y, point, anchor)
        return anchor[0] - dy, anchor[1] + dx

    rects = {}
    # bit masking to record corners touched
    RECT_DELTA, FULL = ((-1, -1, 1), (0, 0, 2), (0, -1, 4), (-1, 0, 8)), 15
    def update_rect(point):
        for dx, dy, mask in RECT_DELTA:
            rx, ry = dx+point[0], dy+point[1]
            if 0 <= rx < 100 and 0 <= ry < 100:
                rects[(rx, ry)] = rects.get((rx, ry), 0) | mask


    HEADING_DELTA = ((1, 0), (0, -1), (-1, 0), (0, 1))
    for ox, oy, heading, gen in curves:
        dx, dy = HEADING_DELTA[heading]
        points = [(ox, oy), (ox+dx, oy+dy)]
        for p in points:
            update_rect(p)

        for _ in range(gen):
            anchor = points[-1]
            for idx in range(len(points)-2, -1, -1):
                new_point = rotate_clockwise(anchor, points[idx])
                update_rect(new_point)
                points.append(new_point)

    return sum(map(lambda x: x == FULL, rects.values()))


N = int(stdin.readline())
curves = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]

print(solution(N, curves))