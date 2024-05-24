

fr = open('meteo_stanice.txt','r')


listik = []
for i in fr.readlines():
    listik.append(i.strip().split(' '))
print(listik)
print(len(listik))


weather = []
for i in listik:
    print(i[3])
    weather.append(i[3])

print(weather)

plus = []
for i in weather:
    if i.startswith('+'):
        x = i.replace(',','.')
        plus.append(float(x.lstrip('+0')))
maximum = max(plus)
print(maximum)

reverse = '+' + str(maximum).replace('.',',')
print(reverse)

for i in listik:
    for j in i:
        if reverse == j:
            print(i[0])

all = []
for i in weather:
    if i.startswith('-'):
        x = float('-'+(i.lstrip('-0')).replace(',','.'))
        all.append(x)
    if i.startswith('+'):
        x = float(i.lstrip('+0').replace(',','.'))
        all.append(x)
print(all)

print(sum(all)/len(all))




