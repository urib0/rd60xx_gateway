#!/usr/bin/env python3

from ast import arg
import sys

# 引数チェック
args = sys.argv
if len(args) == 1:
    raise Exception("missing argument")
elif len(args) > 2:
    raise Exception("too many arguments")
else:
    device_path = args[1]

print(device_path)

