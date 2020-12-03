list = []
f = open("input.txt", "r")
for x in f:
  list.append(int(x))
list.sort()
nList = list
list.reverse
length = len(list)
for x in list:
    print(x) 
i = length - 1
j = 0
result1 = 0
result2 = 0
result = 0
while i > 0:
    while j < length:
        temp1 = list[i]
        temp2 = nList[j]
        if (temp1 + temp2) == 2020:
            result1 = list[i]
            result2 = nList[j]
            result = result1 * result2
            i = 0
            j = length
        elif (temp1 + temp2) < 2020:
            j = j +1
        else:
            i = i - 1
print(result1)
print(result2)
print(result)
quadList = []
i = 0
j = 0
while i < length:
    while j < length:
        quadList.append([nList[i] + nList[j], nList[i], nList[j]])
        j = j + 1
    i = i + 1
quadList.sort
for x in quadList:
    print(x)
i = 0
j = length - 1
result3 = 0
while i < length * length:
    while j > 0:
        temp1 = quadList[i]
        temp2 = list[j]
        if (temp1[0] + temp2) == 2020:
            result1 = temp1[1]
            result2 = temp1[2]
            result3 = temp2
            result = result1 * result2 * result3
            i = length * length
            j = 0
        elif (temp1[0] + temp2) < 2020:
            i = i + 1
        else:
            j = j - 1  
print(result1)
print(result2)
print(result3)
print(result)
        



