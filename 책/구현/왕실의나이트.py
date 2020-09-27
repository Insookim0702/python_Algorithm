def s(position):
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    y = [str(i) for i in range(1, 9)]
    p = list(position)
    count = 8
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx +=2
    yidx +=1
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -=1
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx += 2
    yidx -= 1
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -=1
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx -=2
    yidx +=1
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -=1
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx -=2
    yidx -=1
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -=1
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx -= 1
    yidx -= 2
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -= 1
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx += 1
    yidx -= 2
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -= 1
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx -= 1
    yidx += 2
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -= 1
    xidx = x.index(p[0])
    yidx = y.index(p[1])
    xidx += 1
    yidx += 2
    if xidx > len(x) or yidx > len(y) or yidx < 0 or xidx < 0:
        count -= 1
    return count


print(s('a1'))
