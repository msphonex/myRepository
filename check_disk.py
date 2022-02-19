import psutil
import tkinter as tk


def show_alarm(alarm_text):
    window = tk.Tk()
    window.title('check_disk_alarm')
    window.geometry('400x200')
    lb = tk.Label(
        window,
        text=alarm_text,
        font=('Arial', 19),
    )
    lb.pack()
    window.mainloop()


def check_disk():
    alarm_str = ''
    alarm_count = 0
    disk = psutil.disk_partitions()
    # print(type(disk))
    # print(disk)
    for disk_detail in disk:
        # print("{0}\n".format(disk_detail))
        percent_use = psutil.disk_usage(disk_detail[0])
        # print("{0}\n".format(percent_use))
        if percent_use[3] >= 90:
            alarm_count += 1
            alarm_str = alarm_str + "Alarm! {0} 90% used!\n".format(disk_detail[0])
    if alarm_count > 0:
        show_alarm(alarm_str)


if __name__ == '__main__':
    check_disk()

