import datetime
import re
import os
import pathlib

# PATH_VIDEO = r"F:\code\monitor"
PATH_TEST = r"F:\code\test"
PATH_RAR = r"D:\software\winrar"
LOG_PATH = r"F:\code\test\zip_del.log"


# del rec files
def del_rec(del_file_path, log_path):
    log_file = open(log_path, "a+")
    now = datetime.datetime.now()
    log_file.write("start del files at {0}\n".format(now))
    zip_time = (now - datetime.timedelta(days=6)).strftime('%Y%m%d')
    record_files = os.listdir(del_file_path)
    para = ''
    for file_name in record_files:
        zip_file = re.match(zip_time, file_name)
        if zip_file:
            para += ' ' + file_name
            if os.path.exists("{0}\{1}".format(del_file_path, file_name)) and pathlib.Path(file_name).suffix != '.rar':
                del_file = "{0}\{1}".format(del_file_path, file_name)
                print(del_file)
                os.unlink(del_file)
                log_file.write("{0} has been del\n".format(del_file))
    log_file.write("del success!\n")
    log_file.write("\n")
    log_file.close()



# zip 2days ago rec files
def zip_files(rar_path, zip_file_path, log_path):
    log_file = open(log_path, "a+")
    now = datetime.datetime.now()
    log_file.write("start zip files at {0}\n".format(now))
    zip_time = (now - datetime.timedelta(days=6)).strftime('%Y%m%d')
    # print(now, zip_time)
    # record_files = os.listdir(PATH_VIDEO)
    record_files = os.listdir(zip_file_path)
    # print(record_files)
    para = ''
    for file_name in record_files:
        zip_file = re.match(zip_time, file_name)
        if zip_file and pathlib.Path(file_name).suffix != '.rar':
            para += ' ' + file_name
            log_file.write("{0} will be zip\n".format(file_name))
    # print("para: ", para)
    os.chdir(zip_file_path)
    cur_dir = os.getcwd()
    # print(cur_dir)
    if len(para) > 1:
        cwd = "{0}\Rar.exe a -m5 {1}.rar{2}".format(rar_path, zip_time, para)
        log_file.write(cwd + "\n")
        os_ret = os.system(cwd)
        if os_ret == 0:
            log_file.write("zip success!\n")
            log_file.write("\n")
            log_file.close()
            return True
    log_file.close()
    return False


if __name__ == '__main__':
    zip_ret = zip_files(PATH_RAR, PATH_TEST, LOG_PATH)
    if zip_ret:
        del_rec(PATH_TEST, LOG_PATH)
