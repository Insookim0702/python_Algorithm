def sol(n,plans):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    x, y = 1, 1
    move_types = ['L','R','U','D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x +dx[i]
                ny = y + dy[i]
        if nx < 1 or ny <1 or nx > n or ny > n:
            continue
    print(nx, ny)
    return



print(sol(5, ['R', 'R', 'R', 'U', 'D', 'D']))
