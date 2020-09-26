a =1000
print(a)

a = -8
print(a)

a = 0
print(a)
a = 0.3 + 0.6
print(round(a,1))

if(round(a,1) == 0.9):
    print(True)
else:
    print(False)



a = 7
b =3
print(a/b)
print(a//b)
print(a%b)


a = [1,2,3,4,5,6,7,8]
print(a[-7])
print(a[3:6])

array = [i for i in range(20)]
array = [i+1 for i in range(20)]
array = [i for i in range(20) if i%2==1]
array = [i*i for i in range(1,20)]
n = 3
m = 3
array = [[0] * m] * n
print(array)
array[1][1] = 5
print(array)


array = [[0] * m for _ in range(n)]
print(array)
array[1][1] = 4
print(array)


a = [5,3,23,4,3,5,35,67,567,2]
a.sort(reverse=True)
a.sort()
print(a)


a = [1,2,3,4,5,5,5]
remove_set = [3,5]
result = [i for i in a if i not in remove_set]
print(result)


a = "AVDCODID"
print(a[0:3] *3)

data = dict()
data['사과'] = 'apple'
data['오랜지'] = 'orange'
data['사과'] = 'mingo'
if '사과' in data:
    print('사과 있음.')


key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)
print(data)


score = 30

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')

a = [1,2,3,23]

for i in range(2,10):
    for k in range(1,10):
        print(i,' * ',k,' = ',i*k)
for i in range(3,0,-1):
    print(i)

print((lambda a,b:a+b)(3,7))
print((lambda  a,b,c : a+b-c)(7,3,1))


