# 3:49 ~ 4:17
def solution(dirs):
    answer = 0
    past_load = []
    x = 0
    y = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in dirs:
        if i == 'U':
            xi = x + dx[0]
            yi = y + dy[0]
            if check_right(x, y, xi, yi, past_load, answer):
                load1 = x, y, xi, yi
                load2 = xi, yi, x, y
                if not load1 in past_load or not load2 in past_load:
                    past_load.append(load1)
                    past_load.append(load2)
                    answer += 1
                x = xi
                y = yi
        elif i == 'D':
            xi = x + dx[1]
            yi = y + dy[1]
            if check_right(x, y, xi, yi, past_load, answer):
                load1 = x, y, xi, yi
                load2 = xi, yi, x, y
                if not load1 in past_load or not load2 in past_load:
                    past_load.append(load1)
                    past_load.append(load2)
                    answer += 1
                x = xi
                y = yi
        elif i == 'L':
            xi = x + dx[2]
            yi = y + dy[2]
            if check_right(x, y, xi, yi, past_load, answer):
                load1 = x, y, xi, yi
                load2 = xi, yi, x, y
                if not load1 in past_load or not load2 in past_load:
                    past_load.append(load1)
                    past_load.append(load2)
                    answer += 1
                x = xi
                y = yi
        else:
            xi = x + dx[3]
            yi = y + dy[3]
            if check_right(x, y, xi, yi, past_load, answer):
                load1 = x, y, xi, yi
                load2 = xi, yi, x, y
                if not load1 in past_load or not load2 in past_load:
                    past_load.append(load1)
                    past_load.append(load2)
                    answer += 1
                x = xi
                y = yi

    print(x, ', ', y)
    return answer


def check_right(x, y, xi, yi, past_load, answer):

    if xi > 5 or xi < -5 or yi > 5 or yi < -5:
        return False
    return True


print(solution('ULURRDLLU'))  # 7
print(solution('LULLLLLLU'))  # 7
