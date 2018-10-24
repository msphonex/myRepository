#!/bin/python
#extract message username and password

import os

source_file = '/home/unknown/individual/python/test.txt'

target_file = '/home/unknown/individual/python/user_and_pwd.txt'

f_s = file(source_file)

f_t = file(target_file, 'w')

while True:
    line = f_s.readline()
    if 'ssglog' in line:
