from tkinter import *
from PIL import Image,ImageTk
root=Tk()

IMG=[]
for i in range(1,10):
    im=Image.open(r'output/'+ str(i) +'.png')
    img=ImageTk.PhotoImage(im)
    IMG.append(img)
counter=0
label=Label(root,image=IMG[counter])
label.grid(row=1)

def chimg():
    global label
    global counter
    if counter<10:
        counter+=1
    else:
        counter=0
    label.destroy()
    label=Label(root,image=IMG[counter])
    label.grid(row=1)
    
Button(root,text='Next',command=chimg).grid(row=0)
mainloop()
