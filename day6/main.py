f = open("input.txt", "r")
input = f.read()
groups = input.split("\n\n")
#print(groups)
group = set([])
counts = []
counts2 = []
count = 0
count2 = 0
for x in groups:
    group = set([])
    toDiscard = set([])
    oneGroup = x.split("\n")
    if "" in oneGroup:
        oneGroup.remove("")
    print(oneGroup)
    for y in oneGroup:
        i = 0
        length = len(y)
        while i < length:
            group.add(y[i])
            i = i + 1
    #print(group)
    counts.append(len(group))
    newGroup = group
    for y in oneGroup:
        for z in group:
            if z not in y:
                newGroup = newGroup - set([z])
    counts2.append(len(newGroup))
#print(counts)
for x in counts:
    count = count + x
#print(counts2)
for x in counts2:
    count2 = count2 + x
print(count)
print(count2)
    
    