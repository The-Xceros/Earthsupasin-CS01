from tkinter import *
root = Tk()
root.title("First GUI")
line1 = Label(text="Supasin",fg="blue",font=30).grid(row=0,column=0)
line2 = Label(text="Narksamai",fg="green",font=30).grid(row=1,column=1)
root.geometry("300x300")
root.mainloop()