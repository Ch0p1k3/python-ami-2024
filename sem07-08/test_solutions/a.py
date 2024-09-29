arr = [int(e) for e in input().split() if int(e) != 0]
print(len(arr) - len(set(arr)))
