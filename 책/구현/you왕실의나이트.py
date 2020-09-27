def s(position):
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    y = [str(i) for i in range(1, 9)]
    p = list(position)
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    count = 8
    for step in steps:
        dx = xidx + step[0]
        dy = yidx + step[1]
        if dx > 8 or dy > 8 or dy < 0 or dx < 0:
            count -= 1

    return count


print(s('a1'))
