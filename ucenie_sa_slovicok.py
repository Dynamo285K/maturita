fr = open('ucenie_sa_slovicok.txt','r',encoding='utf-8')

x = fr.readlines()


slovicka_sj = []
for i in x[::2]:
    slovicka_sj.append(i.strip())
print(slovicka_sj)

slovicka_anj = []
for i in x[1::2]:
    slovicka_anj.append(i.strip())
print(slovicka_anj)


def skusac(jazyk):
    wrong_counter = 0
    if jazyk == 'sj':
        while slovicka_sj != []:
            x = input(f'{slovicka_sj[-1]}: ')
            if x == slovicka_anj[-1]:
                slovicka_sj.pop()
                slovicka_anj.pop()
            else:
                wrong_counter += 1
                slovicka_sj.insert(0,slovicka_sj[-1])
                slovicka_sj.pop()
                slovicka_anj.insert(0,slovicka_anj[-1])
                slovicka_anj.pop()
    else:
        while slovicka_anj != []:
            x = input(f'{slovicka_anj[-1]}: ')
            if x == slovicka_sj[-1]:
                slovicka_sj.pop()
                slovicka_anj.pop()
            else:
                wrong_counter += 1
                slovicka_sj.insert(0,slovicka_sj[-1])
                slovicka_sj.pop()
                slovicka_anj.insert(0,slovicka_anj[-1])
                slovicka_anj.pop()
    print(f'Pocet nespravnych odpovedi: {wrong_counter}')

skusac('anjj')


