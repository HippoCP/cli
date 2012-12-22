#!/usr/bin/python3

import argparse
from hippocp.models import User

parser = argparse.ArgumentParser(description='This is a script to manage HippoCP user permissions.')
parser.add_argument('-u', '--user', help='User id', required = True)
parser.add_argument('-l', '--list', help='List permissions', action='store_true')
args = parser.parse_args()

if args.list is True:
	u = User(args.user)
	print(u.permissions())
	