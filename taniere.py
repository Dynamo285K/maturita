import tkinter as tk,random

root = tk.Tk()

canvas = tk.Canvas(root,height=100,width=500)
canvas.pack()

alph = "ABCDEFGHIJ"

tags = []
def taniere():
    global tags
    for i in range(0,10):
        x = canvas.create_oval(20 + i *45,70,20 + i*45 + 40, 30,fill= 'blue')
        tags.append(x)
    for i in range(0,10):
        letter = canvas.create_text((20 + i *45+22), 50,text=alph[i])
    print(tags)



broken  = random.randrange(1,10)


kliknute = []
def check(e):
    global broken, kliknute
    x,y = e.x,e.y
    overlapping = canvas.find_overlapping(x,y,x,y)
    if overlapping[0] == broken:
        canvas.delete('all')
        f = ''.join(kliknute)
        canvas.create_text(250,40,text=f'nasiel si ho a bol to tanier cislo {broken}',font='Arial 15',fill='red')
        canvas.create_text(250,60,text=f'predtym si klikol aj na  {f}',font='Arial 10',fill= 'blue' )
        return
    else:
        kliknute.append(alph[overlapping[0]-1])


taniere()


canvas.bind("<Button-1>", check)

root.mainloop()
