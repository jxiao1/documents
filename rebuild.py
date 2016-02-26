#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

help_no_sphinx = '''
It seems that sphinx is not installed. Please install it firstly.
For example, in the Ubuntu host:
    $ sudo apt-get install sphinx-common python-sphinx texlive
    $ sudo pip install -r ./requirements.txt
'''

if os.system('which sphinx-build 2>/dev/null') != 0:
   print(help_no_sphinx)
   sys.exit(1)

os.system('make html')
os.system('firefox _build/html/index.html')
