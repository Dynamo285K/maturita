from collections import Counter
fr = open('skod_do_dialky.txt','r')



listik = []
for i in fr.readlines():
    listik.append(i.strip().split(' '))
print(listik)


krajiny = []
for i in listik:
    krajiny.append(''.join([i[1]]))
print(krajiny)



pocty = Counter(krajiny)
print(pocty)

krajiny_solo = []
for i in krajiny:
    if i not in krajiny_solo:
        krajiny_solo.append(i)

print(krajiny_solo)

ints = []
for i in listik:
    for j in i[3::]:
        ints.append(int(j))
print(ints)

max = max(ints)
print(max)

vitazi = []
for i in listik:
    if str(max) in i:
        print(i[0])

