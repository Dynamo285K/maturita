import shutil

fr = open('hada.txt')

listik = []

for i in fr.readlines():
    listik.append(i.strip())
print(len(listik))

res = max(listik, key = len)
print(len(res))

shutil.copy('hada.txt', 'hada_copy.txt')

counter = 1
temp_list = []
final_list = []
for i in listik:
    for j in range(1,len(i)):
        char = i[j]
        if i[j] == i[j-1]:
            counter +=1
        else:
            stringos = f'{i[j-1]} {str(counter)} '
            temp_list.append(stringos)
            counter = 1
    stringos = f'{i[j]} {str(counter)} '
    temp_list.append(stringos)
    final_list.append(temp_list)
    temp_list = []
    counter = 1

print(final_list)

fp = open('hada_copy2.txt','w')
for i in final_list:
    fp.write(''.join(i)+ '\n')



