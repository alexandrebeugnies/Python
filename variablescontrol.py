#coding:utf-8
import tkinter
"""
StringVar() : chaine de caractères [str]
IntVar() : nombre entier [int]
DoubleVar(): nombre flottant [float]
BooleanVar(): booléen [bool]
"""
# Observer
def update_label(*args):
	var_label.set(var_entry.get())
	
def update_observer(*args):
	#print("J'ai vu !")
	if var_gender.get():
		var_label_gender.set("C'est un Homme")
	else:
		var_label_gender.set("C'est une Femme")
# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variables tkinter")

# Widgets ...
var_gender = tkinter.IntVar()
var_gender.trace("w", update_observer)
radio1 = tkinter.Radiobutton(app, text = "Homme", value=1, variable=var_gender)
radio2 = tkinter.Radiobutton(app,text = "Femme",value = 0, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label_gender)

var_entry = tkinter.StringVar()
var_entry.trace("w", update_label)
entry = tkinter.Entry(app, textvariable = var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app,width =20, text="Bonjour ! :)",textvariable=var_label)

#var_label.set("Le label ...")

#print("Label :", var_label.get())
radio1.pack()
radio2.pack()
entry.pack()
label.pack()
label_gender.pack()
# Boucle Principale
app.mainloop()
