# 14:09 ~ 14:39
import heapq
n = int(input())

heap = []
for _ in range(n):
    a= int(input())
    heapq.heappush(heap, a)
result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)


