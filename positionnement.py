#coding:utf-8

import tkinter

# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement widgets")

# Widgets
"""
mainframe = tkinter.LabelFrame(app,text = "Titre ")
mainframe.pack()
"""
"""label = tkinter.Label(app, text= "Un label")
ent = tkinter.Entry(app)"""

btn  = tkinter.Button(app, text="BIENVENUE") 
btn.place(x=500,y=10)
"""label.grid(row=0,column=0)
ent.grid(row=0,column=1)
btn.grid(row=0,column=2)"""

# Boucle principale
app.mainloop()

"""
paramètres pack = side,expand,fill,padx,pady,ipadx,ipady.
paramètre grid = row,column,spancolumn,rowspan,padx,pady,sticky
"""
