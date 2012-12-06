#!/usr/bin/python3

import argparse
from hippocp.models import User

parser = argparse.ArgumentParser(description='This is a script to manage HippoCP user roles.')
parser.add_argument('-u', '--user', help='User id', required = True)
parser.add_argument('-l', '--list', help='List roles', action='store_true')
parser.add_argument('-c', '--check', help='Check specific role', action='store_true')
parser.add_argument('-a', '--add-role', help='Add role to the user', action='store_true')
parser.add_argument('-d', '--remove-role', help='Remove role to the user', action='store_true')
parser.add_argument('-r', '--role', help='Role (required for check, add, remove)')
args = parser.parse_args()

if args.list is True:
	u = User(args.user)
	print(u.roles())

if args.check is True:
	u = User(args.user)
	print(u.checkRole(args.role))

if args.add_role is True:
	u = User(args.user)
	print(u.addRole(args.role))

if args.remove_role is True:
	u = User(args.user)
	print(u.removeRole(args.role))