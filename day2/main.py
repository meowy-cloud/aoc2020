f = open("input.txt", "r")
correct = 0
correct2 = 0
for x in f:
    print(x)
    list1 = x.split("-")
    list2 = list1[1].split(" ")
    list3 = list2[1].split(":")
    list4 = list2[2].split("\n")
    args = [list1[0], list2[0], list3[0], list4[0]]
    print(list2)
    print(list1)
    print(args)
    min = int(args[0])
    max = int(args[1])
    occ = args[3].count(args[2])
    print(occ)
    if (min <= occ and occ <= max):
        correct = correct+1
    pos1 = min -1
    pos2 = max -1
    string = args[3]
    if(bool(string[pos1] == args[2]) != bool(string[pos2] == args[2])):
        correct2 = correct2 +1
print(correct)
print(correct2)


