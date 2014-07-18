#!/usr/bin/env python
''' list files in filder and all sub-folders and writing result
	in 000-file_list.txt, located in folder examined.
	feel free to modify, as you see fits
	(c) 2014, D. Djokic. No warranties'''
	
import os
from sys import stdin
import subprocess

path = stdin.read()
os.chdir(path)
filename = "000-file_list.txt"
fn = open(filename, "w")

for root, dirs, files in os.walk (path, topdown=True):
	fn.write (str(root))
	fn.write ("\n")
	fn.write (str(dirs))
	
	for file in files:
		
		fn.write("\n")
		fn.write(str(root)+"/"+str(file))
fn.close()

note_list = path + "/" + filename

if os.sys.platform.startswith('darwin'):
    subprocess.call(('open', note_list))
elif os.name == 'nt':
    os.startfile(note_list)
elif os.name == 'posix':
    subprocess.call(('xdg-open', note_list))
