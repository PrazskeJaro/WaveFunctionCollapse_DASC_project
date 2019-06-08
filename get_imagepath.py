from tkinter import *
from tkinter.filedialog import *

import os

global image_path

image_path = ""

def import_path():
    image_path = askopenfilename()
    #print(len(image_path))
    #print(image_path)
    return image_path

top=Tk()
top.title("WaveFunctionCollapse")
top.geometry("100x60+10+5")

menubar = Menu(top)
filemenu = Menu(top)
filemenu.add_command(label = "导入",command=import_path)
menubar.add_cascade(label="文件",menu=filemenu)



top['menu']=menubar

shortcutbar=Frame(top,height=25,bg='light sea green')
shortcutbar.pack(expand=NO,fill=X)
Inlabe=Label(top,width=2,bg='antique white')
Inlabe.pack(side=LEFT,anchor='nw',fill=Y)

textPad=Text(top,undo=True)
textPad.pack(expand=YES,fill=BOTH)
scroll=Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT,fill=Y)



