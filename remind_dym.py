#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import sys
import tkinter as tk


PATH_PERIOD_FILE = r'F:\code\record_period.txt'


def record_date():
    record_file = open(PATH_PERIOD_FILE, "a+", encoding="utf-8")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    next_today = datetime.datetime.now() + datetime.timedelta(days=28)
    next_today = next_today.strftime("%Y-%m-%d")
    record_file.write("本次危险日为：{0}\t预计下次爆豆日期为：{1}\n".format(today, next_today))
    record_file.close()


def remind_period():
    display_text = open(PATH_PERIOD_FILE, "r", encoding="utf-8")
    rd_line = display_text.readlines()
    display_text.close()
    window = tk.Tk()
    window.title('you known')
    window.geometry('800x400')
    lb = tk.Label(
        window,
        text=rd_line[-1],
        font=('Arial', 19),
        justify="left",
        # width=55,
        # height=5
    )
    lb.place(x=10, y=10)
    tk.Button(window, width=20, height=4, text="today be careful", command=record_date).place(x=200, y=150)
    tk.Button(window, width=20, height=4, text="today is safety", command=window.destroy).place(x=400, y=150)
    window.mainloop()


if __name__ == '__main__':
    remind_period()
