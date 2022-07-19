from tkinter import filedialog
from os import supports_follow_symlinks
from tkinter import *
from tkinter import ImageTk, Image
root=Tk
root.title("kaka")
root.minsize(650, 650)
root.maxsize(650, 650)
open_img = ImageTk.PhotoImage(Image.open ("open.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))
save_png = ImageTk.PhotoImage(Image.open ("save.png"))
Labelfilename= Label(root, text= "filename")
Labelfilename.place(relx=0.46, rely=0.03, anchor=CENTER)
inputfilename= Entry(root)
inputfilename.place(relx=0.46, rely=0.03, anchor=CENTER)
textarea= Text(root, width= 35, height=80)
textarea.place(relx=0.5, rely=0.55, anchor=CENTER)
root.mainloop()