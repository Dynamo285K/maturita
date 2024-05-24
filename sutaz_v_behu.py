fr  = open('sutaz_vbehu.txt','r')


listik = []
for i in fr.readlines():
    listik.append(i.strip().split(' '))
print(f'Počet zúčastnených športovcov: {len(listik)}')

for i in listik:
    print(f'Súťažiaci {i[0]} dobehol do cieľa za {i[1]} sekúnd')

casy = []
for i in listik:
    casy.append(int(i[1]))
x = max(casy)
print(x)

min = x//60
sek = x%60
print(min,sek)
cas = f'{str(min)} min. {str(sek)} sek.'
print(cas)

fp = open('sutaz_vbehu.txt','w')


for i in listik:
    if i[1] == str(x):
        fp.write(f'{i[0]} {i[1]} {cas}\n')
    else:
        fp.write(f'{i[0]} {i[1]}\n')

