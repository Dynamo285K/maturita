
from itertools import groupby
fr = open('kompresia_obrazka.txt','r')

coords = fr.readline().strip().split(' ')
print(coords)


listik = []
for i in fr.readlines():
    listik.append(i.strip().split(' '))
print(len(listik))

new_list = []
def spracuj_riadok():
    temp_list = []
    counter = 0
    for i in listik:
        if ''.join(i).startswith('0'):
            for j in i:
                res = [len(list(r)) for _, r in groupby(j)]
            print(res)
        else:

            for j in i:
                res = [len(list(r)) for _, r in groupby(j)]
            res.insert(0,0)
            print(res)
        new_list.append(res)
    print(new_list)

spracuj_riadok()

fp = open('kompresia_obrazka_vystup.txt','w')

for i in new_list:
    x = [str(j) for j in i]
    x = ' '.join(x)
    print(x)
    fp.write(f'{x} \n')



