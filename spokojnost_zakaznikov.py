from collections import Counter

fr = open('spokojnost.txt','r',encoding='utf-8')

red = fr.readlines()

print(len(red))

list_of_happy_hours = []
list_of_hours = []
list_of_sad_hours = []

for line in red:
    list_of_hours.append(line.strip().split(':')[0])
    split_by_space = line.strip().split(' ')
    if split_by_space[-1] == 'áno':
        list_of_happy_hours.append(line.strip().split(':')[0])
    else:
        list_of_sad_hours.append(line.strip().split(':')[0])


counter_hours = Counter(list_of_hours)
counter_happy_hours = Counter(list_of_happy_hours)
counter_sad_hours = Counter(list_of_sad_hours)

print(f'najviac spokojnych zakaznikov bolo pocas hodiny {counter_happy_hours.most_common()[0][0]} a ich pocet bol {counter_happy_hours.most_common()[0][1]} a najviac nespokojnych zakaznikov bolo pocas hodiny {counter_happy_hours.most_common()[-1][0]} a ich pocet bol {counter_happy_hours.most_common()[-1][1]}')


for i in counter_hours:
    print(f'spokojnost {i} hodiny je {counter_happy_hours.get(i)/counter_hours.get(i)*100}')

