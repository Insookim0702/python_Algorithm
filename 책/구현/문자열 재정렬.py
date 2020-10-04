#10:00 ~10:20
n ='K1KA5CB7'

l = list(n)
l.sort(reverse=True)
print(l)
result = []
value =0
value1 ='0'
print(value1.isdigit())
for i in l:
    if i.isalpha():
        result.append(i)
    else:
        value +=int(i)

result.sort()
if value != 0:
    result.append(str(value))
print((''.join(result)))