#!/usr/bin/python3

import argparse
from hippocp import Users

parser = argparse.ArgumentParser(description='This is a script to list HippoCP users.')
args = parser.parse_args()

u = Users()
print(u.list())