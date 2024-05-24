import tkinter as tk
import random
win = tk.Tk()

canvas = tk.Canvas(height=200,width=300)
canvas.pack()

colors = ['green','red','grey','blue','orange']

ids = []
def kable():
    for i in range(len(colors)):
        ids.append(canvas.create_rectangle(30,50+i*10,150,40+i*10,fill=colors[i]))
    print(ids)

kable()

canvas.create_text(150,20,text='Pyrotechnik',fill='blue',font='Arial 10')
canvas.create_text(150,30,text='Oznac spravny kablik')


time = 60

def time_change(time,timer):
    time -= 1
    if time > 0:
        canvas.itemconfig(timer,text = time)
        timer = win.after(1000, time_change, time, timer)
    else:
        canvas.delete('all')


timer = canvas.create_text(200,70, text = time,font='Arial 20',fill='red')
time_change(time,timer)

def defuse(event):
    x,y = event.x,event.y
    ids = canvas.find_overlapping(x,y,x,y)
    print(ids)
    if ids[0] == right_one:
        canvas.delete('all')
        canvas.create_text(150,100,text='vyhral si',font='Arial 20',fill='red')
    else:
        canvas.delete('all')
        canvas.create_text(150,100,text='vybuch',font='Arial 20',fill='red')


right_one = random.choice([1,2,3,4,5])
print(right_one)
win.bind('<Button-1>',defuse)

win.mainloop()
