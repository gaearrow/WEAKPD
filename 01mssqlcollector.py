# -- coding:utf-8 --
# Python v2.7.10
# mssqlcollector.py
# Written by Gaearrow

import shodan
import sys

# API_KEY
API_KEY = "YOUR_API_KEY"
query = "product:\"Microsoft SQL Server\""

# process input
if len(sys.argv) != 3:
    print 
    print 'Usage: MSSQL.py <page start:1,2...> <page end:1,2...>'
    sys.exit(1)
pagestart = int(sys.argv[1])
pageend = int(sys.argv[2])

try:
    # output files init.
    ofilename = 'page'+str(pagestart)+'to'+str(pageend)
    ofilesrc = ofilename+'_src.txt'
    ofileip = ofilename+'_ip.txt'
    fsrc = open(ofilesrc,'w')
    fip = open(ofileip,'w')

    # for calc.
    numofport = 0
    numofnoport = 0
    rstlist = 0
    
    # process page one by one
    api = shodan.Shodan(API_KEY)
    rsttotal = api.count(query)
    maxpage = (rsttotal['total']+99)/100
    if pageend > maxpage:
        pageend = maxpage
    for page in range(pagestart,pageend+1):
        result = api.search(query,page)
        for mssql in result['matches']:
            # extract ip&port from banner
            ## delete \r\n
            ip = mssql['ip_str'].strip('\n')
            ## ignore IPv6 addr.
            if len(ip) > 15:
                continue
            ## skip random chars
            banner = mssql['data'][3:]
            ## check banner
            if banner.find('ServerName') < 0:
                continue
            pos = banner.find('tcp;')
            if pos > 0:
                strlist = banner[pos:].split(';')
                if strlist[1].find('np') < 0:
                    ### tcp;1234;np;..
                    ipport = ip+':'+strlist[1]
                    numofport = numofport + 1
                else:
                    ### tcp;np;..
                    ipport = ip+":1433"
                    numofnoport = numofnoport + 1
            else:
                ### no 'tcp;'
                ipport = ip+":1433"
                numofnoport = numofnoport + 1

            print >>fip,ipport
            print >>fsrc,mssql['ip_str']
            print >>fsrc,mssql['data'][3:]
            rstlist = rstlist + 1

    # print info.
    print >>fsrc,'==================================='
    print >>fsrc,'Shodan Summary Information @Gaearrow'
    print >>fsrc,'Query : ', query
    print >>fsrc,'Total Results : ', rsttotal['total']
    print >>fsrc,'List  Results : ', rstlist
    print >>fsrc,'Page  Start   : ', pagestart
    print >>fsrc,'Page  End     : ', pageend
    print >>fsrc,'Port  Assigned   : ',numofport
    print >>fsrc,'Port  Unassigned : ',numofnoport
    print >>fsrc,'==================================='
    print '==================================='
    print 'Shodan Summary Information @Gaearrow'
    print 'Query : ', query
    print 'Total Results : ', rsttotal['total']
    print 'List  Results : ', rstlist
    print 'Page  Start   : ', pagestart
    print 'Page  End     : ', pageend
    print 'Port  Assigned   : ',numofport
    print 'Port  Unassigned : ',numofnoport
    print '==================================='

except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)

fsrc.close()
fip.close()
