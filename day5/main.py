f = open("input.txt", "r")
rows = list(range(0, 128))
seats = list(range(0, 8))
row = 0
seat = 0
i = 0
temp = []
temp2 = []
ids = []
for x in f:
    i = 0
    temp = rows
    temp2 = seats
    print(temp2)
    while (i < 7):
        if x[i] == "F":
            temp = temp[:len(temp)//2]
        else:
            temp = temp[len(temp)//2:]
        i = i + 1
    row = temp[0]
    while (i < 10):
        if x[i] == "L":
            temp2 = temp2[:len(temp2)//2]
        else:
            temp2 = temp2[len(temp2)//2:]
        i = i + 1
    seat = temp2[0]
    tempId = row * 8 + seat
    ids.append(tempId)
ids.sort()
print(ids)
print(ids[(len(ids)-1)])
possible = list(range(0, 1024))
missing = set(possible) - set(ids)
print(missing)
for x in missing:
    if (x -1) in ids and (x + 1) in ids:
        print(x)

