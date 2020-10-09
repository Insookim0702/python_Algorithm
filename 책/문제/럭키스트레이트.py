# 15:58 ~ 16:05

n = list(map(int, input()))

m = len(n)
if sum(n[0:m//2]) == sum(n[m//2:m]):
    print('LUCKY')
else:
    print('READY')




