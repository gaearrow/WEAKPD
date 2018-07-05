# -- coding:utf-8 --
# Python v2.7.10
# mssqlextractor.py
# Written by Gaearrow

import sys

# process input
if len(sys.argv) == 1:
   print 'Usage: %s <extract source>' % sys.argv[0]
   sys.exit(1)
srcfile = sys.argv[1].strip()
fsrc = open(srcfile,'r')

try:
    for eachline in fsrc:
        if eachline.find('[mssql]') > -1:
            strlist = eachline.split()
            print strlist[2]+','+strlist[0].strip('[mssql]')+','+strlist[4]+','+strlist[6]
except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)

fsrc.close()
