
from tkinter import *
import tkinter.messagebox as messagebox

t=Tk()
input_word=Entry(t)
input_word.pack()
def hello():
    name=input_word.get() or 'world'
    messagebox.showinfo('message','hello %s' % name)
sb=Button(t,text='确定',command=hello)
sb.pack()

t.mainloop()