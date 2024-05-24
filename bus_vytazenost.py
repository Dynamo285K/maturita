fr = open('bus_vytazenost.txt','r',encoding='utf-8')


listik = []
for i in fr.readlines():
    listik.append(i.strip().split(' '))
print(listik)

zastavky = ''
for i in listik[1::]:
    if len(i) > 3:
        zastavky += i[2] + ' ' + i[3] + ','
    else:
        zastavky += i[2] + ','
print(zastavky)

rekord  = 0
pocet = 0
for i in listik[1::]:
    max = listik[0]
    pocet += int(i[0])
    pocet -= int(i[1])
    if pocet > rekord:
        rekord = pocet
    if pocet > 50:
        print(' '.join(i[2::]))
print(rekord)

