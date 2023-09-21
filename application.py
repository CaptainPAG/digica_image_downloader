import tkinter as t
import tkinter.messagebox as mb
import main
import subprocess
from config import *
import os

root = t.Tk()

def validate(list):
    try:
        l = eval(list)
        return True
    except NameError:
        mb.showerror("parse error", "parse error. confirm your input text")
        return False

def submit():
    value = entiry.get()
    if validate(value):      
        list = eval(value)
        # 配列の1つ目にｎ不要なテキストがい含まれているので削除する
        del list[0]
        main.main(list=list)
        path = fr"{os.getcwd()}\cards"
        subprocess.Popen(['explorer', path], shell=True)

root.title = "Deck Image Transfer"

x, y = 300, 400
root.minsize(y, x)
root.geometry(f"{y}x{x}")
root.title("digica image downloader")

label = t.Label(root, text="IMPORT text by generated Deck Builder")
label.pack(pady=10, padx=10)

entiry = t.Entry(root, width=50,)
entiry.pack()

button = t.Button(root, text="submit", command=submit)
button.pack(pady=10)

result_l = t.Label(root, text=os.getcwd(), wraplength=200)
result_l.pack()

root.mainloop()