import tkinter as tk
from tkinter.ttk import *
from turtle import bgcolor, color
from functools import partial
import billboard

window = tk.Tk()
style = Style()
style.configure('My.TFrame', background='#1d1d1d')
window.geometry('350x200')
window.title("TuneFinder v1.0")

tab_control = Notebook(window)

#Songs
tab1 = Frame(tab_control, style='My.TFrame')

tab_control.add(tab1, text='Songs')
songlbl = Label(tab1, text= 'Top Songs', font=("Arial", 11, "bold"), anchor='w', background='#1d1d1d')
songlbl.grid(sticky = "w", column=0,row=0)
songlbl.config(background='#1d1d1d', foreground="WHITE")

chart = billboard.ChartData('hot-100')
song = chart[0]
songList = []
recList = []

i = 0
while (i < 100):
    songList.append(chart[i].title)
    i = i+1


def likeSong(id):
    id = id-1
    recList.append(chart[id].title)
    print("Added " + chart[id].title)
    #print(recList[1])


songid = 0
for s in songList:
    songid = songid+1
    displaylabel = Label(tab1, text = s, background='#1d1d1d', font=("Arial", 10, "bold"))
    displaylabel.grid(sticky = "w", column = 0, row = songid)
    displaylabel.config(background = '#1d1d1d', foreground="WHITE")

    style2 = Style()
    style2.configure("flat.TButton", foreground="WHITE", background="#1d1d1d")

    action_with_arg = partial(likeSong, songid)
    displaybutton = Button(tab1, text = "Like", style = "flat.TButton", command = action_with_arg)
    displaybutton.grid(sticky = "e", column = 7, row = songid)



#Reccomended
tab2 = Frame(tab_control, style='My.TFrame')
tab_control.add(tab2, text='Reccomended')
reclbl = Label(tab2, text= 'Reccomended Songs', font=("Arial", 11, "bold"), anchor='w', background='#1d1d1d')
reclbl.grid(sticky = "w", column=0, row=0)
reclbl.config(background='#1d1d1d', foreground="WHITE")

recList.append("STARS")
recid = 0
for r in recList:
    recid = recid+1
    displaylabel2 = Label(tab2, text = r, background='#1d1d1d', font=("Arial", 10, "bold"))
    displaylabel2.grid(sticky = "w", column = 0, row = recid)
    displaylabel2.config(background = '#1d1d1d', foreground="WHITE")





#Top Genres
tab3 = Frame(tab_control)
tab_control.add(tab3, text='Top Genres')

lbl3 = Label(tab3, text= 'label3')

lbl3.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')



window.mainloop()