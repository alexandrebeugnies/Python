#coding:utf-8

import tkinter
#from tkinter import *

mainapp = tkinter.Tk()
mainapp.title("Mon premier programme")
#mainapp.resizable(width=False, height=True)
"""
mainapp.minsize(640,480)
mainapp.maxsize(1280,720)
"""
#mainapp.geometry("800x600+50+100")

"""
mainapp.positionfrom("user")
mainapp.sizefrom("user")
"""
screen_x = mainapp.winfo_screenwidth()
screen_y = mainapp.winfo_screenheight()
window_x = 800
window_y = 600

position_X = (screen_x//2) - (window_x //2)
position_Y = (screen_y//2) - (window_y //2)
geo = "{}x{}+{}+{}".format(window_x, window_y, position_X, position_Y)
mainapp.geometry(geo)
mainapp.mainloop()

#mainapp.quit()





















































































