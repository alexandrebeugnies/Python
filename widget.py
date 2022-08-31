#coding:utf-8
"""
<nom_variable> = <nom_widget>(<widget_parent>, <params> ...)
"""

import tkinter
app = tkinter.Tk()
"""
label_welcome = tkinter.Label(app, text = "Bonjour et Bienvenue à tous !")
message_welcome = tkinter.Message(app, text = "Bonjour et Bienvenue à tous !")
#label_welcome["text"]
print(label_welcome.cget("text"))
label_welcome.configure(text="Nouveau Message")

label_welcome.pack()
message_welcome.pack()
"""
entry_name = tkinter.Entry(app, width = 45, show = "*",exportselection=0 )
entry_name.pack()

def hello():
	print("Hello sur le terminal !!!")
button_quit = tkinter.Button(app, text = "OK", width = 25, height = 5,command = hello)
button_quit.pack()
app.mainloop()
