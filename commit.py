#!/usr/bin/python3

import sys
import os
import subprocess
from traceback import print_tb
file_name = sys.argv[1]
message = sys.argv[2]
os.system('echo commiting changes for {0}'.format(file_name))
print("+-+-+-+-+-+-+-+-+-+-+-+-")
print("")
os.system('git add {0}'.format(file_name))
os.system('git commit -m "{0}"'.format(message))
os.system('git push')
print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-")
os.system('echo completed remote update')
