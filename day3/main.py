f = open("input.txt", "r")
array = []
length = 0
for x in f:
    line = []
    length = len(x) - 1
    i = 0
    while i < length:
        line.append(x[i])
        i = i + 1
    array.append(line)
    print(line)
    print(length)
i = 0
j = 0
first1 = 0
first2 = 0
firstTree = 0
third1 = 0  
third2 = 0
thirdTree = 0
fourth1 = 0
fourth2 = 0
fourthTree = 0
fifth1 = 0
fifth2 = 0
fifthTree = 0
trees = 0
while i < len(array):
    temp = array[i]
    if temp[j] == '#':
        trees = trees + 1
    i = i + 1
    j = (j + 3) % length
print(trees)
while first1 < len(array):
    temp = array[first1]
    if temp[first2] == '#':
        firstTree = firstTree + 1
    first1 = first1 + 1
    first2 = (first2 + 1) % length
print(firstTree)
while third1 < len(array):
    temp = array[third1]
    if temp[third2] == '#':
        thirdTree = thirdTree + 1
    third1 = third1 + 1
    third2 = (third2 + 5) % length
print(thirdTree)
while fourth1 < len(array):
    temp = array[fourth1]
    if temp[fourth2] == '#':
        fourthTree = fourthTree + 1
    fourth1 = fourth1 + 1
    fourth2 = (fourth2 + 7) % length
print(fourthTree)
while fifth1 < len(array):
    temp = array[fifth1]
    if temp[fifth2] == '#':
        fifthTree = fifthTree + 1
    fifth1 = fifth1 + 2
    fifth2 = (fifth2 + 1) % length
print(fifthTree)
result = firstTree * trees * thirdTree * fourthTree * fifthTree
print(result)

      