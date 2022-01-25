import os
import datetime
import re
import pathlib
import shutil

PATH_SRC = r"//192.168.50.108/movie/monitor"
PATH_DES = r"G:\rec_files_after_2022"
PATH_LOG = r"F:\code\move_rec_file.log"


def move_file(des_path, src_path, log_path):
    # exp_file = os.listdir(src_path)
    # print (exp_file)
    log_file = open(log_path, "a+")
    now = datetime.datetime.now()
    log_file.write("start move files at {0}\n".format(now))
    log_file.flush()
    move_time = (now - datetime.timedelta(days=4)).strftime('%Y%m%d')
    record_files = os.listdir(src_path)
    # print("record files:", record_files)
    if not os.path.exists("{0}\{1}".format(des_path, move_time)):  # if dir not exist then mkdir
        os.mkdir("{0}\{1}".format(des_path, move_time))
        log_file.write("mkdir {0}\{1} success!\n".format(des_path, move_time))
    des_path_dir = "{0}\{1}".format(des_path, move_time)
    # print("des_path_dir:", des_path_dir)
    for file_name in record_files:  # re match two days ago rec files then move them
        move_files = re.match(move_time, file_name)
        if move_files:
            if os.path.exists("{0}\{1}".format(src_path, file_name)) and pathlib.Path(file_name).suffix == '.avi':
                move_file_src = "{0}/{1}".format(src_path, file_name)
                move_file_des = "{0}\{1}".format(des_path_dir, file_name)
                # print("move_file_src:", move_file_src, "\tmove_file_des:", move_file_des)
                shutil.move(move_file_src, move_file_des)
                log_file.write("{0} has been moved\n".format(move_file_src))
                log_file.flush()
    log_file.write("move files finished at {0}!\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    log_file.write("\n")
    log_file.close()


if __name__ == '__main__':
    move_file(PATH_DES, PATH_SRC, PATH_LOG)
