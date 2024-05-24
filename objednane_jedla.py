from collections import Counter
fr = open('objednane_jedla.txt')



listik = []
for i in fr.readlines():
    listik.append(i.strip().split(' '))
# print(listik)
print(f'pocet vsetkych obedov: {len(listik)}')


obedy = []
for i in listik:
    obedy.append(i[1])
# print(obedy)

pocty = Counter(obedy)
print(f'pocty jednotlivych jedal: {pocty}')

temp = []
for key, value in pocty.items():
    if value < 20:
        temp.append(key)
print(f'toto jedlo si objednalo menej ako 20 ludi: {temp}')




