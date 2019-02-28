#Simple Interest Calculator using Tkinter
from tkinter import *
from math import *

def simple_interest():
    #float(principle.get())
    #float(rate.get())
    #int(time.get())
    print("Principle: %s\nRate: %s \nTime: %s" % (principle.get(), rate.get(), time.get()))
    #print("Simple Interest is:" % (principle.get()* rate.get()* time.get())/100
    #return
    #print("Simple interest value: " + "{0:.2f}".format(simple_interest));

root = Tk()
Label(root, text="PRINCIPLE").grid(row=0)
Label(root, text="RATE").grid(row=1)
Label(root, text="TIME").grid(row=2)

principle = Entry(root)
rate = Entry(root)
time = Entry(root)

principle.insert(10, 0)
rate.insert(10, 0)
time.insert(10, 0)

principle.grid(row=0, column=1)
rate.grid(row=1, column=1)
time.grid(row=2, column=1)

Button(root, text='Calculate', command=simple_interest).grid(row=4, column=2, sticky=W, pady=4)
Button(root, text='Quit', command=root.quit).grid(row=4, column=3, sticky=W, pady=4)

mainloop( )
