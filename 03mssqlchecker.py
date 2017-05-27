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

# for stats.
nsqlser = 0
ncmdenable = 0
ncmddisable = 0

# check one by one
for eachline in fsrc:

    # check input format.
    if eachline.count(';') != 3:
       print >>fsql,eachline
       continue
    nsqlser = nsqlser + 1
    strlist = eachline.strip().split(';')
    print >>fsql,strlist[0]+';',
    print 'Checking '+strlist[0]

    # connect sql server
    try:
       conn = pymssql.connect(host=strlist[0],user=strlist[2],password=strlist[3],database='master',port=strlist[1],login_timeout=30,charset='utf8')
       cursor = conn.cursor()
       print >>fsql,'online;',
    except Exception as e:
        #print 'Error: %s' % e
        print >>fsql,'offline;',
        continue

    # get xp_cmdshell status
    try:
        cursor.execute("exec sp_configure 'xp_cmdshell'")
        xpcmd = cursor.fetchall()
        if xpcmd[0][3] == 1:
            print >>fsql,'Enabled'+';',
            ncmdenable = ncmdenable + 1
        else:
            print >>fsql,'Disabled'+';',
            ncmddisable = ncmddisable + 1
    except Exception as e:
        #print 'Error: %s' % e
        print >>fsql,'Disabled'+';',
        ncmddisable = ncmddisable + 1

    # get sql version
    try:
        cursor.execute("select @@version;")
        sqlinfo = cursor.fetchall()
        sqlverno = sqlinfo[0][0].split('\n\t')[0]
        sqlvno = sqlverno.split('-')[1]
        sqlver = sqlverno.split('-')[0]
        osver = sqlinfo[0][0].split('on')[-1].strip()
        print >>fsql,sqlver+';'+sqlvno+';'+osver
    except Exception as e:
        #print 'Error: %s' % e
        conn.close()
        continue
       
    conn.close()

print '==================================='
print 'MSSQL Check Information @Gaearrow'
print 'Total Target : ', nsqlser
print 'Cmdshell Enabled  : ', ncmdenable
print 'Cmdshell Disabled : ', ncmddisable
print '==================================='

fsrc.close()
fsql.close()

