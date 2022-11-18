#!/usr/bin/env python3

from ast import arg
import sys

from rd6006 import RD6006

# 引数チェック
args = sys.argv
if len(args) == 1:
    raise Exception("missing argument")
elif len(args) > 2:
    raise Exception("too many arguments")
else:
    device_path = args[1]

# rd60xxと疎通確認
device = RD6006(device_path)
print(f"model:{device.type}")
print(f"fw:{device.fw}")
device.enable = False
print(f"output:{True if device.enable == 1 else False }")

