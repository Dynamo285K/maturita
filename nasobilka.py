import random

x = [random.randrange(1,11) for i in range(1,11)]
y = [random.randrange(1,11) for i in range(1,11)]

results = []
for i in range(len(x)):
    results.append(x[i]*y[i])

points = 0
max_points = 10
while results != []:
    entry = input(f'vypocitaj:  {x[-1]} * {y[-1]}\n')
    if int(entry) == results[-1]:
        # print('spravne')
        x.pop()
        y.pop()
        results.pop()
        if max_points > 0:
            points += 1
            max_points -= 1
    else:
        # print('nespravne')
        x.insert(0,x[-1])
        y.insert(0,y[-1])
        results.insert(0,results[-1])
        x.pop()
        y.pop()
        results.pop()
        max_points -= 1

if results == []:
    print(f'Vypocitane s poctom bodov {points}')

