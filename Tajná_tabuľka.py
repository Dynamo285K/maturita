from collections import Counter
kod = [[' '],['ABC'],['DEF'],['GHI'],['JKL'],['MNO'],['PQR'],['STU'],['VWX'],['YZ']]

string = ''
poradie = -1
input = 'AKO SA MAS'
for i in input:
    for j in kod:
        poradie += 1
        x = ''.join(j)
        if i in x:
            counter = x.index(i) + 1
            string += counter*str(poradie) + ' '
    poradie = -1
print(string)

x = Counter(string).most_common()
print(x)
print(f'Najčastejšie zvolené políčka: {x[1][0]}')

