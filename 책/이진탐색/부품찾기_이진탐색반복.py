h = 6
length = [19,15,10,17]
length = [19,14,10,17]
length.sort()

def binary_search(start, end):
    while start <= end:
        mid = (start + end) //2
        if length()[mid] ==target:
            return mid
