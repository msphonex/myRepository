#!/bin/python

import os
import sys

def get_filename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        if root == file_dir:
            for name in files:
                if "ex" in name:
                    print(name)

if __name__ == "__main__":
    get_filename(sys.argv[1])
