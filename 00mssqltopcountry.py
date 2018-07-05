# -- coding:utf-8 --
# Python v2.7.10
# mssqltopcountry.py
# Written by Gaearrow

import shodan
import sys

# MY_API_KEY
API_KEY = "YOUR_API_KEY"

# The list of properties we want summary information on
FACETS = [
    ('country', 50),
]

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)

    # Perform the search
    query = "product:\"Microsoft SQL Server\""
    result = api.count(query,facets=FACETS)

    print '==================================='
    print 'Shodan Summary Information'
    print 'Query: %s' % query
    print 'Total Results: %s' % result['total']
    print '==================================='
    print 'Top 50 Countries\n'
    for term in result['facets']['country']:
        print '%s: %s' % (term['value'], term['count'])
    print '==================================='
    
except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)

