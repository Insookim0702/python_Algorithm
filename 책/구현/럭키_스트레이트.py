
#9:52~ 10 :00(8분)

n = 123402
l = list(map(int, str(n)))
helf = len(l) // 2
left = sum(l[:helf])
right = sum(l[helf:len(l)])

if left == right:
    print('LUCKY')
else:
    print('READY')

