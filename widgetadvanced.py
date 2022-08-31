#coding:utf-8

import tkinter
from tkinter import messagebox
"""
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel
"""
#import tkMessagebox (old version)
def show_modal_window():
	messagebox.showerror("ERREUR", "Un Problème est survenu !")
app = tkinter.Tk()
"""
check_widget = tkinter.Checkbutton(app,text= "Publier ?", offvalue = 2, onvalue=5)
radio_widget = tkinter.Radiobutton(app,text = "Homme", value = 1)
radio_widget2 = tkinter.Radiobutton(app, text= "Femme", value = 0)
check_widget.pack() 
radio_widget.pack()
radio_widget2.pack()
"""
"""
scale_w = tkinter.Scale(app, from_=10, to=100, tickinterval=25)
spin_w = tkinter.Spinbox(app, from_=1,to=10)

scale_w.pack()
spin_w.pack()
"""
"""
lb = tkinter.Listbox()
lb.insert(1, "Windows")
lb.insert(2, "GNU/Linux")
lb.insert(3, "MacOS")

lb.pack()
"""
btn = tkinter.Button(app, text ="Déclencher une erreur", command=show_modal_window)
btn.pack()
app.mainloop()
