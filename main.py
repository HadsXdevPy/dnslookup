import sys
from os import system
try:
    import tkinter
    import requests
    from tkinter import *
    from tkinter import filedialog
    from bs4 import BeautifulSoup
except:
    sys.exit(0.1)
    system('pip3 install tk')
    system('pip3 install requests')
    system('pip3 install bs4')
    system('python3 main.py')

root = Tk()
root.title('DNS LOOKUP(HadiJembod)')
root.config(background='#fff')

root.geometry('720x450')
root.columnconfigure(0, weight=1)

def dns():
    req=requests.get('https://api.hackertarget.com/dnslookup/?q='+url.get())
    result = Label(root,
        text=req.text,
        fg='#000',
        bg='#fff')
    result.grid(pady=1)
def exit():
    root.destroy()

frame = tkinter.Frame(root)
frame.grid(row=0,column=0)

run = Button(frame,
    width=20,
    text='run dns',
    command=dns)
run.grid(row=0,column=0)

run = Button(frame,
    width=20,
    text='run dns',
    command=dns)
run.grid(row=0,column=0)

exits = Button(frame,
    width=20,
    text='exit',
    command=exit)
exits.grid(row=0,column=1)

url_var = StringVar()
url = Entry(root,
    width=40,
    justify='center',
    textvariable=url_var)
url.grid(pady=1)

author = Label(root,
    text='DNS LOOKUP',
    fg='#d00000',
    bg='#fff',
    font=('Roboto', 18))
author.grid(pady=1)

root.mainloop()
