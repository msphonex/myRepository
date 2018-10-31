#!/bin/python
#extract message username and password

import os

source_file = '/home/unknown/individual/python/test.txt'

target_file = '/home/unknown/individual/python/user_and_pwd.txt'

f_s = open(source_file)

f_t = open(target_file, 'w')

while True:
    line = f_s.readline()
    if len(line) == 0:
        break
    if 'sshlog' in line:
        line_list = line.split()
        if len(line_list) == 7:
            f_t.write(line_list[6]+'\n')
        else:
            f_t.write(line_list[6]+' '+line_list[7]+'\n')
f_s.close
f_t.close
