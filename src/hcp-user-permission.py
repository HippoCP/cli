#!/usr/bin/python3

import argparse
from hippocp.models import User

parser = argparse.ArgumentParser(description='This is a script to manage HippoCP user permissions.')
parser.add_argument('-u', '--user', help='User id', required = True)
parser.add_argument('-l', '--list', help='List permissions', action='store_true')
parser.add_argument('-c', '--check', help='Check specific permission', action='store_true')
parser.add_argument('-a', '--add-permission', help='Add permission to the user', action='store_true')
parser.add_argument('-d', '--remove-permission', help='Remove permission to the user', action='store_true')
parser.add_argument('-r', '--permission', help='Permission (required for check, add, remove)')
args = parser.parse_args()

if args.list is True:
	u = User(args.user)
	print(u.permissions())

if args.check is True:
	u = User(args.user)
	print(u.checkPermission(args.permission))

if args.add_permission is True:
	u = User(args.user)
	print(u.addPermission(args.permission))

if args.remove_permission is True:
	u = User(args.user)
	print(u.removePermission(args.permission))