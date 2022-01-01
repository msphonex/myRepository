#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import sys
import tkinter

def showMessage(who=None):
    window = tkinter.Tk()
    window.title('remind birthday')
    window.geometry('800x400')
    lb = tkinter.Label(
        window,
        text='Today is {} birthday!'.format(who),
        font=('Arial', 23),
        width=55,
        height=5
    )
    lb.pack()
    window.mainloop()

n_time = datetime.datetime.now().strftime('%Y%m%d')
subdate = n_time[4:8]

if subdate == '1118':
    showMessage('myself')
elif subdate == '0804':
    showMessage('mother')
elif subdate == '1121':
    showMessage('father')
elif subdate == '1201':
    showMessage('honey')
else:
    sys.exit()
