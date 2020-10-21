# 투 포인터 : 리스트에 순차적으로 접해야 할 떄 두 개의 점의 위치를 기록하면서 처리하는 알고리즘
# 투 포인터 알고리즘이 자주 사용되는 문제는 "특정한 합을 가지는 부분 연속 수열 찾기 문제"이다.

n = 5
m = 5
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    # end을 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    # 부분합이 m일 때 카운트는 증가
    if interval_sum == m:
        count += 1

    interval_sum -= data[start]

print(count)