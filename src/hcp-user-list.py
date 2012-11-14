#!/usr/bin/python3

import argparse
from hippocp.models import User

parser = argparse.ArgumentParser(description='This is a script to list HippoCP users.')
args = parser.parse_args()

u = User()
print(u.list())