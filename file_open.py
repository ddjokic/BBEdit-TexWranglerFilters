#!/usr/bin/python

# open file, given full path in TextWrangler
 
from sys import stdin
import os
import subprocess

source = stdin.read()
 
if os.sys.platform.startswith('darwin'):
    subprocess.call(('open', source))
elif os.name == 'nt':
    os.startfile(source)
elif os.name == 'posix':
    subprocess.call(('xdg-open', source))