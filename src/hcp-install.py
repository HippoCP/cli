#!/usr/bin/python3

import postgresql
import argparse

from hippocp import settings

parser = argparse.ArgumentParser(description='This is the script to install HippoCP.')
parser.add_argument('-u', '--user', help='Database username', required=True)
parser.add_argument('-p', '--password', help='Database password', required=True)
parser.add_argument('-d', '--database', help='Database name', required=True)
parser.add_argument('-H', '--host', help='Database hostname', required=False, default='localhost')
parser.add_argument('-P', '--port', help='Database port', required=False, default='5432')
args = parser.parse_args()

#Check the connection
url = 'pq://' + args.user + ':' + args.password + '@' + args.host + ':' + args.port + '/' + args.database
try:
    db = postgresql.open(url)
except (postgresql.exceptions.AuthenticationSpecificationError,
        postgresql.exceptions.ClientCannotConnectError):
    print('Invalid database data')
    exit()

#Set here the db vars on config file
settings.set('pgsql', 'hostname', args.host)
settings.set('pgsql', 'username', args.user)
settings.set('pgsql', 'database', args.database)
settings.set('pgsql', 'password', args.password)
settings.set('pgsql', 'port', args.port)

# Create user table
q = 'CREATE TABLE users ('
q+= '    uid integer PRIMARY KEY,'
q+= '    name varchar(30),'
q+= '    package integer,'
q+= '    father integer);'
db.execute(q)

# Create packages table
