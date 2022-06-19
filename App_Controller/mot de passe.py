from tkinter import *
window= Tk()
window.title("yassine")
window.geometry("400x320")
window.minsize(400,320)
window.config(background="blue")

Entry_pass = Entry(window,font=("Arial",20),bg="grey",fg="black",width=20,show="*")
Entry_pass.pack(expand=YES)
window.mainloop()
