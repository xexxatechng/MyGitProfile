#!/usr/bin/python
from tkinter import *
import pymysql


#connect to DB
conn= pymysql.connect(host='localhost', user='root', db='test')

#Create a cursor
curs=conn.cursor()

#Root level form
class MyApp:
    def __init__(self):
        window=Tk()
        window.title('Data Entry Form')
        frame=Frame(window)
        frame.pack()

        #Begin Fields
        self.fields={}

        lab=Label(frame, text="vendID:")
        lab.grid(row=0, column=0)
        self.fields['vendID'] = Entry(frame)
        self.fields['vendID'].grid(row=0, column=1)

        lab=Label(frame, text="vendName:")
        lab.grid(row=2, column=0)
        self.fields['vendName'] = Entry(frame)
        self.fields['vendName'].grid(row=2, column=1)
        #End Fields

        #Begin Buttons
        clearbtn = Button(frame, text="Clear", command=self.do_clear)
        clearbtn.grid(row=11, column=0)

        submitbtn = Button(frame, text="Submit", command=self.do_insert)
        submitbtn.grid(row=11, column=1)

        updatebtn = Button(frame, text="Update", command=self.do_update)
        updatebtn.grid(row=11, column=2)
        #End Buttons

        window.mainloop()

        ## CLEAR, INSERT, and UPDATE functions
    def do_clear(self):
        self.feilds['vendID'].delete(0, END)
        self.feilds['vendName'].delete(0, END)

    def do_insert(self):
        global curs
        sql = "insert into vendor (vendID, vendName) value ('%s', '%s'); "%(self.fields['vendID'].get(), self.fields['vendName'].get())
        curs.execute(sql)
        #print sql

    def do_update(self):
        global curs
        sql="update vendor set vendName='%s' where vendID='%s'; "%(self.fields['vendName'].get(), self.fields['vendID'].get())
        curs.execute(sql)
        #print sql


if __name__=="__main__":
    MyApp()
