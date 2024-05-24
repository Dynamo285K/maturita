import tkinter as tk
import math
win = tk.Tk()

canvas = tk.Canvas(width=500,height=500)
canvas.pack()



dict = {'c':80,'d':75,'e':70,'f':65,'g':60,'a':55,'h':50}
zoz = []

fr = open('noty.txt','r')
line = fr.readline().strip()
print(line)
for i in line:
    zoz.append(i)
print(zoz)

for i in range(int(math.ceil(len(zoz)/20))):
    for j in range(5):
        canvas.create_line(0,30+10*j+i*100,500,30+10*j+i*100)


counter = 1
ciara = 0
for i in zoz:
    canvas.create_oval(-15+counter*25,dict[i]+ciara*100-5,counter*25,dict[i]+ciara*100+5)
    counter +=1
    if counter == 21:
        ciara +=1
        counter = 1


win.mainloop()
