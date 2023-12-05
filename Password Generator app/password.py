from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title('Random Password Generator')
root.geometry("500x300")


def new_rand():
    pw_entry.config(state=NORMAL)
    pw_entry.delete(0, END)
    pw_length = int(num_entry.get())

    my_password = ''

    for i in range(pw_length):
        my_password += chr(randint(33,126))
    pw_entry.insert(0, my_password)
    pw_entry.config(state=DISABLED)


def copy():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Password Generator","Copied to Clipboard..!")

sp = LabelFrame(root, text = "How Many Characters?",font=("Lucida Sans",10,"bold"),fg="#ff0000")
sp.pack(pady=20)

num_entry = Entry(sp,font=("Helvetica",24), bd=0, bg="systembuttonface")
num_entry.pack(pady=20,padx=20)

pw = Label(root,text= "Password",font=("Lucida Sans",10,"bold"),fg="#ff0000")
pw.pack(pady=1,padx=1,side=TOP)

pw_entry = Entry(root, text='', font=("Helvetica",20))
pw_entry.pack(pady=10)

frame = Frame(root)
frame.pack(pady=20)

my_button = Button(frame, text="Generate Password",font=("Helvetica",10,"bold"),command=new_rand,bg="#464EB8",border=5,fg="white")
my_button.grid(row=0, column=0, padx=10)

copy_button = Button(frame, text="Copy",command=copy,font=("Helvetica",10,"bold"), bg="#464EB8", border=5, foreground="white")
copy_button.grid(row=0,column=1, padx=10)

root.mainloop()