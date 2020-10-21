n = list(map(int, input()))
helf = int(len(n) / 2)
f = n[0:helf]
e = n[helf:len(n)]
if sum(f) == sum(e):
    print("LUCKY") 
else:
    print("READY")

