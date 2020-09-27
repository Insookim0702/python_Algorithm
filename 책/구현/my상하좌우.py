def sol(n, arr):
    p = [1, 1]
    for i in arr:
        if i == 'R':
            if p[1] != 5:
                p[1] += 1
            continue
        if i == 'L':
            if p[1] != 1:
                p[1] -= 1
            continue
        if i == 'U':
            if p[0] != 1:
                p[0] -= 1
            continue
        if i == 'D':
            if p[0] != 5:
                p[0] += 1
            continue

    return p


print(sol(5, ['R', 'R', 'R', 'U', 'D', 'D']))
