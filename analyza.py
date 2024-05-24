from collections import Counter
fr = open('spokojnost.txt','r',encoding='utf-8')

lines = fr.readlines()
print(f'Pocet vsetlkych vyjadreni: {len(lines)}')

delimiters = [":", " "]
final_temp = []
for i in lines:
    x = i.strip().replace(':',' ')
    result = x.split(' ')
    final_temp.append(result)
# print(final_temp)

temp1 = 0
temp2 = 0
counter = 1
daily_counter = 0
day_counter = 0
for i in final_temp:
    r = int(i[0])
    f = int(i[1])
    if r > temp1 or r == temp1 and f >= temp2:
        temp1 = int(i[0])
        temp2 = int(i[1])
        daily_counter += 1
    else:
        print(f'{counter}. deň - počet reakcií: {daily_counter}')
        daily_counter =1
        counter +=1
        temp1 = int(i[0])
        temp2 = int(i[1])
print(counter-1)

hodiny = []
for i in final_temp:
    hodiny.append(i[0])

pocty = Counter(hodiny)

for key,value in pocty.items():
    print(f'Hodina:{key} Reakcií zákazníkov:{value}')

print(f'Pocet dni: {counter-1}')
