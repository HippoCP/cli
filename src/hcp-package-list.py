#!/usr/bin/python3

import argparse

from hippocp import Package

parser = argparse.ArgumentParser(description='This is a script to list HippoCP packages.')
parser.add_argument('-s', help='List system packages', action='store_true', default=True)
parser.add_argument('-u', '--user', help='List packages for a specific user', required=False, default=None)
args = parser.parse_args()

pack = Package()
print(pack.list(args.user, args.s))

