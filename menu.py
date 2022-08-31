#coding:utf-8

import tkinter
def show_about():
	about_window = tkinter.Toplevel(app)
	about_window.title("A propos")
	lb = tkinter.Label(about_window, text="Bonjour")
	lb.pack()
# Création de la fenêtre et paramétrage
app = tkinter.Tk()
app.geometry("640x480")
app.title("Création de Menu")

# Widgets ...
mainmenu= tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu,tearoff=0)
first_menu.add_command(label="Option1")
first_menu.add_command(label="Option2")
first_menu.add_separator()
first_menu.add_command(label="Quitter", command=app.quit)

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="Command1")
second_menu.add_command(label="à propos", command=show_about)

mainmenu.add_cascade(label="Premier", menu=first_menu)
mainmenu.add_cascade(label="Second", menu=second_menu)


# Boucle Principale
app.config(menu=mainmenu)
app.mainloop()
