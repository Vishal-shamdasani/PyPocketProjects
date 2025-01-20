import tkinter as tk
import pyscreenshot

def screenshot():
    img=pyscreenshot.grab()
    img.show()


main=tk.Tk()

main.title("pyScreenshot")

button=tk.Button(main,text="take screenshot",command=screenshot)
button.pack()
main.mainloop()
