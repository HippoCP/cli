#!/usr/bin/python3

import argparse
from hippocp import Roles

parser = argparse.ArgumentParser(description='This is a script to manage HippoCP user roles.')
parser.add_argument('-l', '--list', help='List roles', action='store_true')
args = parser.parse_args()

if args.list is True:
	r = Roles()
	print(r.list())