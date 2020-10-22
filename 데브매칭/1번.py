from collections import deque
from datetime import datetime, timedelta
def solution(n, customers):
    answer = 0
    kiosc = []
    for i in range(n):
        kiosc.append([0, ''])
    print(kiosc)
    cus = deque()
    for i in customers:
        arrive_date , arrive_time, spand_time = i.split()
        m, d = arrive_date.split('/')
        h,mm,s = arrive_time.split(':')
        time = datetime(2020,int(m), int(d), int(h),int(mm),int(s))
        cus.append((time, int(spand_time)))
    print(cus)

    for i in cus:
        print(i[0], '->' ,i[0] + timedelta(minutes=i[1]))




    return answer




print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))