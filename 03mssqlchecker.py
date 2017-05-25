# -- coding:utf-8 --
# Python v2.7.10
# pymssql-2.1.1.win32-py2.7.exe (md5)
# https://pypi.python.org/pypi/pymssql/2.1.1#downloads
# mssqlchecker.py
# Written by Gaearrow

import pymssql
import sys

# process input
if len(sys.argv) == 1:
   print 'Usage: %s <check source>' % sys.argv[0]
   sys.exit(1)
srcfile = sys.argv[1].strip()
fsrc = open(srcfile,'r')
fsql = open('sqlchecklist.txt','w')

for eachline in fsrc:
    strlist = eachline.strip().split(';')
    print >>fsql,strlist[0]+';',
    try:
       conn = pymssql.connect(host=strlist[0],user=strlist[2],password=strlist[3],database='master',port=strlist[1],login_timeout=30,charset='utf8')
       cursor = conn.cursor()
    except Exception as e:
        #print 'Error: %s' % e
        print >>fsql,'offline;',
        continue

    print >>fsql,'online;',

    # get xp_cmdshell status
    cursor.execute("exec sp_configure 'show advanced option'")
    advopt = cursor.fetchall()
    if advopt[0][3] == 0:
        print >>fsql,'Disabled'+';',
    else:
        cursor.execute("exec sp_configure 'xp_cmdshell'")
        xpcmd = cursor.fetchall()
        if xpcmd[0][3] == 1:
            print >>fsql,'Enabled'+';',
        else:
            print >>fsql,'Disabled'+';',
    # get sql version
    cursor.execute("select @@version;")
    sqlinfo = cursor.fetchall()
    sqlverno = sqlinfo[0][0].split('\n\t')[0]
    sqlvno = sqlverno.split('-')[1]
    sqlver = sqlverno.split('-')[0]
    osver = sqlinfo[0][0].split('on')[-1].strip()
    print >>fsql,sqlver+';'+sqlvno+';'+osver
        
    conn.close()

fsrc.close()
fsql.close()

