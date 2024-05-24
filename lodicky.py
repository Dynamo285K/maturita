import tkinter as tk, random
root = tk.Tk()

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    plachta_id = canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    boat_id = canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)
    return boat_id,plachta_id

boats = []

def start_race():
    global ciara, boats
    ciara = canvas.create_line(650,0,650,800,fill='red')
    for i in range(1,16):
        boats.append(lodicka(50,20 + 50*i))
    print(boats)
    movement()

def movement():
    global ciara, boats
    for plachta_id,boat_id in boats:
        moving = random.randrange(1,10)
        canvas.move(plachta_id,moving,0)
        canvas.move(boat_id,moving,0)
        print()
        if canvas.coords(boat_id)[4] > 650:
            canvas.delete(ciara)
            canvas.create_text(350,400,text=f'vyhrala lodka {int(boat_id/2)}!', font= 'Arial 15')
            return
    canvas.after(50,movement)


canvas = tk.Canvas(root, width=700, height=800)
canvas.pack()

bt = tk.Button(root,text='start',command=start_race)
bt.pack()
root.mainloop()
