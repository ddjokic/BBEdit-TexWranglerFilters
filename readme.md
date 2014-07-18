### BBEdit/TextWrangler Text Filters

Few python scripts to be located in **/Users/Username/Library/Application Support/TextWrangler/Text Filters** and executed from BBEdit or TextWrangler menu *Apply Text Filter*.

To do any action, highlight text in editor and execute the action on it. To highlight/select text in editor use mouse or "shift-command-right arrow". I am using this combo to help me with my text/markdown notes.

Text Filters:

file_open.py - opens file which name **and** path are highlighted in BBE or TW
filelist_tw.py - lists all files in the folder (folder must be selected in BBE/TW)
srchtxtdir_tw.py - search for highlighted text in all text files located in a folder which name is hardcoded
tag_list.py - I put my tags inside the file, as first line, beginning with "#". This script retrieve all tags

First two scripts are creating list files in working folder. 

#####Note:
For some reason scripts remove selected line. Just undo the action after executing them, as delete is last action executed.

#####Disclaimer:
Use all scripts on your own risk.

(C) D. Djokic, 2014