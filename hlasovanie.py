from collections import Counter

fr = open('hlasovanie.txt','r')

listik = []
for i in fr.readlines():
    listik.append(i.strip())
print(len(listik))

x = Counter(listik)

for key,value in x.items():
    print(f'{key} : {value}')



if Counter(x).most_common()[-1][-1] == Counter(x).most_common()[-2][-1]:
    print(f'{Counter(x).most_common()[-2]}  {x.most_common()[-1]}')
else:
    print(x.most_common()[-1])

fp = open('hlasovanie_vypadnuti.txt','r')
f = [i.strip() for i in fp.readlines()]
# print(f)

for i in f:
    del x[i]
# print(x)
print(x.most_common()[-1])
