from datetime import datetime, timedelta
def solution(p,n):
    answer = ""
    a, time = p.split()
    print(a)
    h, mm, s = time.split(':')
    time = datetime(2020, 8, 3, int(h), int(mm), int(s))
    jug =  datetime(2020, 8, 3, 12, 0, 0)
    new_time = time + timedelta(seconds=n)
    if a == 'PM':
        if new_time.time() <= jug.time():
            new_time = new_time + timedelta(hours=12)
        else:
            new_time = new_time + timedelta(hours=24)
    else:
            new_time = new_time + timedelta(hours=12)

    print(time, '->', new_time)
    date, time = str(new_time).split()
    return time



print(solution("PM 01:00:00", 10))
print(solution("PM 11:59:59", 1))
print(solution("AM 12:01:00", 1))
print(solution("PM 12:01:00", 1))