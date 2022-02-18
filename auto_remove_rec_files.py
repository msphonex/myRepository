import datetime
import shutil
import os

PATH_LOG = r"F:\code\auto_remove_rec_files.log"
PATH_REMOVE = r"G:\rec_files_after_2022"


def auto_remove_rec(remove_path, log_path):
    log_file = open(log_path, "a+")
    now = datetime.datetime.now()
    log_file.write("start remove files at {0}\n".format(now.strftime('%Y%m%d %H:%M:%S')))
    log_file.flush()
    remove_time = (now - datetime.timedelta(days=30)).strftime('%Y%m%d')
    remove_des_path = "{0}\{1}".format(remove_path, remove_time)
    log_file.write("{0} will be removed\n".format(remove_des_path))
    if os.path.exists(remove_des_path):
        shutil.rmtree(remove_des_path)
        log_file.write("{0} has been removed at {1}\n".format(remove_des_path, datetime.datetime.now().strftime(
            "%Y%m%d %H:%M:%S")))
    else:
        log_file.write("dir not exist no file has been removed\n")
    log_file.write("remove files finished at {0}!\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    log_file.write("\n")
    log_file.close()


if __name__ == '__main__':
    auto_remove_rec(PATH_REMOVE, PATH_LOG)
