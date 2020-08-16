from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("1420x820+0+0")
l=Label(text='label1',fg='red',bg='blue',font=20).pack()
l1=Label(text='label2',fg='blue',bg='yellow',font=20).pack()

def hello():
    c=Label(text="hello").pack()
button1=Button(text='enter',fg='blue',bg='red',command=hello,font=20).pack()
a.mainloop()


