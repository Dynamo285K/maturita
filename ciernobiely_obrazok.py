# import tkinter as tk
# win = tk.Tk()
#
# current_color = 'black'
#
# def vykresli(farba):
#     with open('komprimovany_obrazok.txt', 'r') as fr:
#         coords = fr.readline().strip().split()
#         width, height = int(coords[0]), int(coords[1])
#
#         canvas.delete("all")
#
#         x, y = 0, 0
#         if farba == 'neagativ':
#             counter = 1
#         else:
#             counter = 0
#
#         for line in fr:
#             for g in line.strip().split(' '):
#                 color = 'black' if counter == 0 else 'white'
#                 for _ in range(int(g)):
#                     canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)
#                     x += 1
#                     if x >= width:
#                         x = 0
#                         y += 1
#                 counter = 1 - counter
#
# def change_color():
#     global current_color
#     current_color = 'neagativ' if current_color == 'black' else 'black'
#     vykresli(current_color)
#
#
# coords = open('komprimovany_obrazok.txt', 'r').readline().strip().split()
# canvas = tk.Canvas(win, width=int(coords[0]), height=int(coords[1]))
# canvas.pack()
#
#
# vykresli(current_color)
#
#
# btn = tk.Button(win, text="Change Color", command=change_color)
# btn.pack()
#
# win.mainloop()

import tkinter as tk
win = tk.Tk()

coords = open('komprimovany_obrazok.txt', 'r').readline().strip().split()
canvas = tk.Canvas(win, width=int(coords[0]), height=int(coords[1]))
canvas.pack()

base_color = 'white'

def vykresli(base_color):
    with open('komprimovany_obrazok.txt', 'r') as fr:
        coords = fr.readline().strip().split()
        width = int(coords[0])
        height = int(coords[1])

        canvas.delete('all')

        if base_color == 'black':
            counter = 1
        else:
            counter = 0
        color = ''
        x, y = 0, 0

        for i in fr:
            for g in i.strip().split():
                if counter == 0:
                    color = 'black'
                else:
                    color = 'white'
                for r in range(int(g)):
                    canvas.create_rectangle(x,y,x+1,y+1,fill=color,outline=color)
                    x+=1
                    if x >= width:
                        x = 0
                        y += 1
                counter = 1 - counter

def change_color():
    global base_color
    if base_color == 'white':
        base_color = 'black'
    else:
        base_color = 'white'
    vykresli(base_color)


vykresli(base_color)

button = tk.Button(win,text='reforma',command=change_color)
button.pack()


win.mainloop()
