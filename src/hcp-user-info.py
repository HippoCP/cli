#!/usr/bin/python3

import argparse
from hippocp.models import User

parser = argparse.ArgumentParser(description='This is a script to list HippoCP user info.')
parser.add_argument('-u', '--user', help='User id', required = True)
parser.add_argument('-r', help='List roles', action='store_true', default=True)
args = parser.parse_args()

u = User(args.user)
print(u.roles())