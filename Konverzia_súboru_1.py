
fr = open('ciernobiely_obrazok_1.txt','r')

coords = fr.readline().strip().split(' ')
listik = []
for i in fr.readlines():
    listik.append(i.strip())
print(listik)

final_list = []
for i in listik:
    x = [i[j:j+2] for j in range(0, len(i), 2)]
    final_list.append(x)
    print(final_list)



list_zeroes_one = []
temp_list = []
for i in final_list:
    for j in i:
        deci = int(j, 16)
        print(deci)
        if deci > 127:
            temp_list.append('1')
        else:
            temp_list.append('0')
    list_zeroes_one.append(temp_list)
    temp_list = []
print(list_zeroes_one)

fp = open('konverzia_suboru_1_vystup.txt','w')

coords_string = ' '.join(coords)
fp.write(f'{coords_string}\n')
for i in list_zeroes_one:
    stringos = ' '.join(i)
    fp.write(f'{stringos}\n')
