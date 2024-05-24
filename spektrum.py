from collections import Counter
import tkinter as tk
root = tk.Tk()

fr = open('ciernobiely_obrazok_1.txt','r')

coords = fr.readline().strip().split()
print(coords)

canvas = tk.Canvas(width= int(coords[0])*2,height=500)
canvas.pack()


n = 2
double = []
for line in fr.readlines():
    line = line.strip()
    double.append([line[i:i+n] for i in range(0, len(line), n)])
print(double)

final_list = []
for i in double:
    for j in i:
        final_list.append(j)

counter = Counter(final_list)
print(counter.items())

canvas = tk.Canvas(width= len(counter)*2,height=500)
canvas.pack()

x_counter = 0
for key,value in counter.items():
    canvas.create_rectangle(x_counter,500,x_counter+2,500-value,fill='grey',outline='grey')
    x_counter += 2

root.mainloop()

