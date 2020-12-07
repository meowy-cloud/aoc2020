import re
f = open("input.txt", "r")
input = f.read()
individ = input.split("\n\n")
counter = 0
toContain = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for i in individ:
    if all(x in i for x in toContain):
        counter = counter + 1
print(counter)
counter2 = 0
fieldsCorrect = []
for i in individ:
    #print(i)
    #print("\n")
    fieldsCorrect = []
    fields = re.split(" |\n", i)
    if "" in fields:
        fields.remove("")
    if all(x in i for x in toContain):
        for a in fields:
            oneField = a.split(":")
            key = oneField[0]
            value = oneField[1]
            if key == "byr" and int(value) >= 1920 and int(value) <= 2002:
                fieldsCorrect.append(True)
            elif key == "byr":
                fieldsCorrect.append(False)
            elif key == "iyr" and int(value) >= 2010 and int(value) <= 2020:
                fieldsCorrect.append(True)
            elif key == "iyr":
                fieldsCorrect.append(False)
            elif key =="eyr" and int(value) >= 2020 and int(value) <= 2030:
                fieldsCorrect.append(True)
            elif key == "eyr":
                fieldsCorrect.append(False)
            elif key == "hgt" and ("cm" in value or "in" in value):
                if "cm" in value:
                    value = value[:-2]
                    if int(value) >= 150 and int(value) <= 193:
                        fieldsCorrect.append(True)
                    else:
                        fieldsCorrect.append(False)
                else:
                    value = value[:-2]
                    if int(value) >= 59 and int(value) <=76:
                        fieldsCorrect.append(True)
                    else:
                        fieldsCorrect.append(False)
            elif key == "hgt":
                fieldsCorrect.append(False)
            elif key == "hcl" and "#" in value and len(value[1:]) == 6 and re.match("([0-9]|[a-f])*", value[1:]):
                fieldsCorrect.append(True)
            elif key == "hcl":
                fieldsCorrect.append(False)
            elif key == "ecl" and (value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth"):
                fieldsCorrect.append(True)
            elif key == "ecl":
                fieldsCorrect.append(False)
            elif key == "pid" and len(value) == 9 and re.match("[0-9]*", value):
                fieldsCorrect.append(True)
            elif key == "pid":
                fieldsCorrect.append(False)
            elif key == "cid":
                fieldsCorrect.append(True)
    if len(fieldsCorrect) == len(fields) and all(x == True for x in fieldsCorrect):
        counter2 = counter2 + 1
    #print(fields)
    #print("\n")
print(counter2)
