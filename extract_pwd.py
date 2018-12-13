#!/bin/python
#extract message username and password

import os
import sys

source_file = []
target_file = '/home/unknown/individual/python/user_and_pwd.txt'

def get_filename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        if root == file_dir:    #only get current dir
            for name in files:
                if "message" in name:
                    source_file.append(os.path.join(root, name))
    print(source_file)
    return source_file

if __name__ == "__main__":
    file_dir = sys.argv[1]    
    source_file = get_filename(file_dir)
    for name in source_file:
        f_s = open(name)
        f_t = open(target_file, 'a')
        while True:
            line = f_s.readline()
            if len(line) == 0:
                break
            if 'sshlog' in line:
                line_list = line.split()
                if len(line_list) == 7:
                    f_t.write(line_list[6]+ ' ' + '' + '\n')
                else:
                    f_t.write(line_list[6]+ ' ' + line_list[7] + '\n')
        f_s.close
        f_t.close
    f_target = open(target_file,'r')
    list_of_target = f_target.readlines()
    list_result=list(set(list_of_target))
    f_target.close
    f_write_result = open(target_file, 'w')
    f_write_result.writelines(list_result)
    f_write_result.close
