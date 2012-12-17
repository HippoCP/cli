#!/usr/bin/python3

import argparse
from hippocp import Roles

parser = argparse.ArgumentParser(description='This is a script to manage HippoCP user roles.')
parser.add_argument('-l', '--list', help='List roles', action='store_true')
parser.add_argument('-a', '--add', help='Add role', action='store_true')
parser.add_argument('-r', '--remove', help='Remove role', action='store_true')
parser.add_argument('-i', '--id', help='Role (required for remove)')
parser.add_argument('-n', '--name', help='Role (required for add)')
args = parser.parse_args()

if args.list is True:
	r = Roles()
	print(r.list())

if args.add is True:
	r = Roles()
	print(r.add(args.name))

if args.remove is True:
	r = Roles()
	print(r.remove(args.id))
