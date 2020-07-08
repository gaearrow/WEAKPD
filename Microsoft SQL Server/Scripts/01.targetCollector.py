# -- coding:utf-8 --
# Python v2.7.10
# python TargetCollector.py <limit=MaxResult,optional>
# @Gaearrow

import shodan
import sys

# API_KEY
API_KEY = "<YOUR API KEY>"
query = "product:mssql"

# process input
if len(sys.argv) > 2:
    print 
    print 'Usage: python TargetCollector.py <limit=MaxResult,optional>'
    sys.exit(1)
if len(sys.argv) == 2:
    limit = int(sys.argv[1])
else:
    limit = 100000

try:
    # Check Total Results
    api = shodan.Shodan(API_KEY)
    total = api.count(query)['total']
    if limit > total:
        limit = total
        
    # Output Files Names
    ofilename = 'results_'+str(limit)
    ofilesrc = ofilename+'_src.txt'
    ofileip = ofilename+'_ip.txt'
    fsrc = open(ofilesrc,'w')
    fip = open(ofileip,'w')

    # For Calc.
    numofport = 0
    numofnoport = 0
    rstlist = 0
    
    for mssql in api.search_cursor(query,retries=30):
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
        if rstlist >= limit:
            break

    # Print Info.
    print '==================================='
    print 'Shodan Summary Information @Gaearrow'
    print 'Query : ', query
    print 'Total Results : ', total
    print 'List  Results : ', rstlist
    print 'Port  Assigned   : ',numofport
    print 'Port  Unassigned : ',numofnoport
    print 'Output File Name : ',ofileip
    print 'Output File Name : ',ofilesrc
    print '==================================='

except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)

fsrc.close()
fip.close()
