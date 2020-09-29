
students = [('홍길동', 96),('이순신', 30)]
def setting(data):
    return data[1]

result = sorted(students, key=setting)

result = sorted(students, key=lambda students: students[1])
for i in result:
    print(i[0], end=" ")