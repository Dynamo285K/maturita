import tkinter as tk
root = tk.Tk()


canvas = tk.Canvas(width=250,height=150)
canvas.pack()

colors = ['green','red','blue','yellow']
col = ['g','r','b','y']

for i in range(4):
    canvas.create_rectangle(25+i*50,100,25+i*50+50,50,fill= colors[i])

fr = open('vyber_jedla.txt','w')


def write(e):
    x,y = e.x,e.y
    overlapping = canvas.find_overlapping(x,y,x,y)
    print(overlapping)
    if overlapping != ():
        fr.write(f'{entry.get()} {col[overlapping[0]-1]} \n')
        print(entry.get(), col[overlapping[0]-1])

entry = tk.Entry()
entry.pack()

root.bind('<Button-1>',write)


root.mainloop()









