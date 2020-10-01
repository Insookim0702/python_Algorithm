h = 6
length = [19,15,10,17]
length = [19,14,10,17]

length.sort()
sum_length = 0
max_length = max(length)
result = 0
while True:
    for i in length:
        if max_length < i:
            sum_length += i - max_length
    if sum_length ==6:
        break
    else:
        sum_length = 0
        max_length -=1

print(max_length)







