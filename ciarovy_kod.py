import tkinter as tk,random
win = tk.Tk()

# canvas = tk.Canvas( height=250,width=250,bg='white')
# canvas.pack()
#
#
# fr = open('ciarovy_kod1.txt','r')
# x =fr.readlines()
#
# barcodes = []
# for i in x:
#     barcodes.append(i.strip())
# print(barcodes)
#
#
# def divide_chunks(l, n):
#     for i in range(0, len(l), n):
#         yield l[i:i + n]
#
# final_list = list(divide_chunks(barcodes, 4))
# print(final_list)
#
# counter = -1
# def start(event):
#     global counter
#     canvas.delete('all')
#     counter += 1
#     if counter <len(final_list):
#         posli_kod(final_list[counter])
#
#
# def vytvor_kod(kod,x,y):
#     for i in range(len(kod)):
#         if i == 0:
#             canvas.create_rectangle(15+i*11+x,120+y,15+i*11+int(kod[i])+x,20+y,fill='black')
#         elif i == 7:
#             canvas.create_rectangle(15+i*11+x,120+y,15+i*11+int(kod[i])+x,20+y,fill='black')
#         else:
#             canvas.create_rectangle(15+i*11+x,100+y,15+i*11+int(kod[i])+x,20+y,fill='black')
#         canvas.create_text(55+x,110+y,text=kod,font='Arial 9')
#
# def posli_kod(kody):
#     for i in range(len(kody)):
#         if i == 0:
#             vytvor_kod(kody[i],0,0)
#         elif i == 1:
#             vytvor_kod(kody[i],120,0)
#         elif i == 2:
#             vytvor_kod(kody[i],0,120)
#         else:
#             vytvor_kod(kody[i],120,120)
#
#
# win.bind('<space>', start)
# win.mainloop()


canvas = tk.Canvas(width=250,height=250)
canvas.pack()

fr = open('ciarovy_kod1.txt','r')


listik = []
for i in fr.readlines():
    listik.append(i.strip())
print(listik)

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


n = 4

final_list = list(divide_chunks(listik, n))
print (final_list)

counter = -1
def start(e):
    global counter
    canvas.delete('all')
    counter +=1
    if counter < len(final_list):
        posli_kod(final_list[counter])


def posli_kod(kody):
    for i in range(len(kody)):
        if i == 0:
            nakresli(kody[i],0,0)
        elif i == 1:
            nakresli(kody[i],120,0)
        elif i == 2:
            nakresli(kody[i],0,120)
        elif i == 3:
            nakresli(kody[i],120,120)

def nakresli(kod,x,y):
    for i in range(len(kod)):
        if i == 0:
            canvas.create_rectangle(30+x,120+y,30+x+int(kod[i]),30+y,fill='black')
        elif i == 7:
            canvas.create_rectangle(30+x+i*11,120+y,30+x+i*11+int(kod[i]),30+y,fill='black')
        else:
            canvas.create_rectangle(30+x+i*11,100+y,30+x+i*11+int(kod[i]),30+y,fill='black')
        canvas.create_text(30+x+40,110+y,text=kod)
win.bind('<space>',start)
win.mainloop()
