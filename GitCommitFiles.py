#!/usr/bin/python3
import sys,os
from datetime import datetime
DtTimestr=datetime.now().strftime('%d-%m-%Y-%H%M%S')
msg1='Line no 10 added '+DtTimestr
gtCmd='git commit -m "'+ msg1 +'"'
#print('git commit -m "'+ msg1 +'"')
os.system('git add Document1.txt')
os.system(gtCmd)

