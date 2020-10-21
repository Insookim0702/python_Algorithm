n = list(input())

result = []
sum = 0
for i in n:
    if i.isalpha():
        result.append(i)
    else:
        sum += int(i)

result.sort()

if sum !=0:
    print("".join(result)+str(sum))
else:
    print(result)