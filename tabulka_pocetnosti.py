from collections import Counter
import string


alph = string.ascii_uppercase
fr = open('tabulka_pocetnosti.txt','r')

x = fr.readlines()

splitted = []
for i in x:
    splitted.append(i.strip().split())
print(splitted)

final_list = []
for i in splitted:
    for j in i:
        for r in j.upper():
            final_list.append(r)

# print(final_list)


dict = Counter(final_list)
# print(dict)

print(f'Pocty jednotlivych znakov v texte:')
not_used = []
for i in alph:
    # if i in dict:
    #     print('ye')
    # else:
    #     print('nah')
    if i in dict:
         print(f'{i} - {dict.get(i)}')
    else:
        not_used.append(i)
        print(f'{i} - 0')
print(', '.join(not_used))
