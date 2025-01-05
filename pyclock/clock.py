from tkinter import *
from tkinter.ttk import *

from time import strftime
root= Tk()
root.title("Clock")
label=Label(root,font=("ds-digital",100),background="black",foreground="lime")
label.pack(anchor="center")
def time():
    string=strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
time()
mainloop()
