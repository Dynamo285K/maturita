import tkinter as tk
win = tk.Tk()
fr = open('preklopenie_obrazka.txt','r',encoding='utf-8')
x = fr.readline().strip().split(' ')
print(x)

pixels = []
for i in fr.readlines():
    pixels.append(i.strip().split(' '))
print(pixels)

canvas = tk.Canvas(width=int(x[0]),height=int(x[1]))
canvas.pack()

status = 1

def kresli():
    global status
    y_counter = 0
    x_counter = 0
    if status == 1:
        canvas.delete('all')
        for i in pixels:
            y_counter +=1
            for j in i:
                x_counter +=1
                if j == '1':
                    canvas.create_rectangle(x_counter,y_counter,x_counter+1,y_counter+1,fill='black')
            x_counter = 0
        status = 2
    else:
        canvas.delete('all')
        for i in pixels:
            y_counter +=1
            for j in reversed(i):
                x_counter +=1
                if j == '1':
                    canvas.create_rectangle(x_counter,y_counter,x_counter+1,y_counter+1,fill='black')
            x_counter = 0
        status = 1


btn = tk.Button(win, text = 'Preklop',command = kresli)
btn.pack(side = 'bottom')

kresli()

win.mainloop()
