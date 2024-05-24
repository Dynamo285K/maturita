from random import shuffle
fr = open('poprehadzovany_text.txt','r',encoding='utf-8')

text_list = []
for i in fr.readlines():
    text_list.append(i.strip().split(' '))
print(text_list)

final_list = []
temp_list = []
for i in text_list:
    for j in i:
        if len(j) > 2:
            x = list(j[1:-1:])
            shuffle(x)
            print(x)
            temp_word = j[0] + ''.join(x) + j[-1]
            temp_list.append(temp_word)
        else:
            temp_list.append(j)
    final_list.append(temp_list)
    temp_list = []
print(final_list)

fp = open('poprehadzovany_text_final.txt','w',encoding='utf-8')

for i in final_list:
    line = ' '.join(i)
    fp.write(f'{line} \n')
