#!/usr/bin/python3

import argparse
from hippocp import User

parser = argparse.ArgumentParser(description='This is a script to add HippoCP users')
parser.add_argument('-n', '--name', help='User name', required = True)
parser.add_argument('-p', '--password', help='User password', required = True)
parser.add_argument('-P', '--package', help='Package ID', required = True)
parser.add_argument('-f', '--father', help='Father UID', required = True)
args = parser.parse_args()

u = User()
print(u.add(args.name, args.package, args.father, args.password))