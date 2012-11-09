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

# Clean the db if is not empty
q = 'drop schema public cascade;'
db.execute(q)
q = 'create schema public;'
db.execute(q)

# Create anagraphic table
q = 'CREATE TABLE anagraphics ('
q+= '    id integer PRIMARY KEY,'
q+= '    name varchar(30),'
q+= '    surname varchar(30),'
q+= '    email varchar(30),'
q+= '    address varchar(30),'
q+= '    zip varchar(30),'
q+= '    state varchar(30),'
q+= '    country varchar(30),'
q+= '    phone varchar(30),'
q+= '    taxcode varchar(30)'
q+= ');'

db.execute(q)

# Create packages table
q = 'CREATE TABLE packages ('
q+= '    id SERIAL PRIMARY KEY,'
q+= '    name varchar(40) NOT NULL,'
q+= '    owner integer NOT NULL,'
q+= '    harddisk integer NOT NULL,'
q+= '    bandwidth integer NOT NULL,'
q+= '    domain integer NOT NULL,'
q+= '    subdomain integer NOT NULL,'
q+= '    email integer NOT NULL,'
q+= '    ftp integer NOT NULL'
q+= ');'

db.execute(q)

# Create user table
q = 'CREATE TABLE users ('
q+= '    uid integer PRIMARY KEY,'
q+= '    name varchar(30),'
q+= '    package_id integer,'
q+= '    anagraphic_id integer,'
q+= '    father_id integer'
q+= ');'

db.execute(q)

q = 'ALTER TABLE users'
q+= '    ADD CONSTRAINT FK_user_package'
q+= '    FOREIGN KEY (package_id) REFERENCES packages(id)'
q+= '    ON UPDATE CASCADE'
q+= '    ON DELETE CASCADE'
q+= ';'

db.execute(q)

q = 'ALTER TABLE users'
q+= '    ADD CONSTRAINT FK_user_anagraphic'
q+= '    FOREIGN KEY (anagraphic_id) REFERENCES anagraphics(id)'
q+= '    ON UPDATE CASCADE'
q+= '    ON DELETE CASCADE'
q+= ';'

db.execute(q)

# Create role table
q = 'CREATE TABLE roles ('
q+= '    id SERIAL PRIMARY KEY,'
q+= '    name varchar(30)'
q+= ');'

db.execute(q)

# Create permissions table
q = 'CREATE TABLE permissions ('
q+= '    id SERIAL PRIMARY KEY,'
q+= '    name varchar(30)'
q+= ');'

db.execute(q)

# Create the permission_roles table
q = 'CREATE TABLE permission_role ('
q+= '    permission_id integer,'
q+= '    role_id integer'
q+= ');'

db.execute(q)

q = 'ALTER TABLE permission_role'
q+= '    ADD CONSTRAINT FK_permission_role_permission'
q+= '    FOREIGN KEY (permission_id) REFERENCES permissions(id)'
q+= '    ON UPDATE CASCADE'
q+= '    ON DELETE CASCADE'
q+= ';'

db.execute(q)

q = 'ALTER TABLE permission_role'
q+= '    ADD CONSTRAINT FK_permission_role_role'
q+= '    FOREIGN KEY (role_id) REFERENCES roles(id)'
q+= '    ON UPDATE CASCADE'
q+= '    ON DELETE CASCADE'
q+= ';'

db.execute(q)

# Create the permission_user table
q = 'CREATE TABLE permission_user ('
q+= '    permission_id integer,'
q+= '    user_id integer'
q+= ');'

db.execute(q)
