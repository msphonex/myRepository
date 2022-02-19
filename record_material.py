#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import sys
import tkinter as tk
from functools import partial

RECORD_FILE_PATH=r'D:\material\record_material.txt'


def sub_time(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y%m%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date2, "%Y%m%d %H:%M:%S")
    return date2 - date1


def double_kill(start_time, rec_date):
    record_file = open(RECORD_FILE_PATH, "a+")
    end_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
    record_file.write("{0} {1} double kill\n".format(rec_date, sub_time(start_time, end_time)))
    record_file.close()


def triple_kill(start_time, rec_date):
    record_file = open(RECORD_FILE_PATH, "a+")
    end_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
    record_file.write("{0} {1} triple kill\n".format(rec_date, sub_time(start_time, end_time)))
    record_file.close()


def quadra_kill(start_time, rec_date):
    record_file = open(RECORD_FILE_PATH, "a+")
    end_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
    record_file.write("{0} {1} quadra kill\n".format(rec_date, sub_time(start_time, end_time)))
    record_file.close()


def penta_kill(start_time, rec_date):
    record_file = open(RECORD_FILE_PATH, "a+")
    end_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
    record_file.write("{0} {1} penta kill\n".format(rec_date, sub_time(start_time, end_time)))
    record_file.close()


def funny(start_time, rec_date):
    record_file = open(RECORD_FILE_PATH, "a+")
    end_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
    record_file.write("{0} {1} funny\n".format(rec_date, sub_time(start_time, end_time)))
    record_file.close()


def weird(start_time, rec_date):
    record_file = open(RECORD_FILE_PATH, "a+")
    end_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
    record_file.write("{0} {1} weird\n".format(rec_date, sub_time(start_time, end_time)))
    record_file.close()


def record_material(start_time, rec_date):
    window = tk.Tk()
    window.title('record material')
    window.geometry('400x200')
    tk.Button(window, width=20, height=2, text="double kill", command=partial(double_kill, start_time, rec_date)).grid(row=1, column=1)
    tk.Button(window, width=20, height=2, text="triple kill", command=partial(triple_kill, start_time, rec_date)).grid(row=1, column=2)
    tk.Button(window, width=20, height=2, text="quadra kill", command=partial(quadra_kill, start_time, rec_date)).grid(row=2, column=1)
    tk.Button(window, width=20, height=2, text="penta kill", command=partial(penta_kill, start_time, rec_date)).grid(row=2, column=2)
    tk.Button(window, width=20, height=2, text="funny", command=partial(funny, start_time, rec_date)).grid(row=3, column=1)
    tk.Button(window, width=20, height=2, text="weird", command=partial(weird, start_time, rec_date)).grid(row=3, column=2)
    window.mainloop()


if __name__ == '__main__':
    record_file_main = open(RECORD_FILE_PATH, "a+")
    record_file_main.write("\n")
    record_file_main.close()
    now = datetime.datetime.now()
    start_time_now = now.strftime("%Y%m%d %H:%M:%S")
    record_date = now.strftime("%Y%m%d")
    record_material(start_time_now, record_date)
