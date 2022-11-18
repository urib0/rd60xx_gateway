#!/usr/bin/env python3

from rd6006 import RD6006
import json

# 設定値読み込み
with open("./config.json", "r") as f:
    conf = json.loads(f.read())

device_path = conf["serialDevice"]
ip = conf["ipAddress"]
port = conf["port"]

# rd60xxと疎通確認
device = RD6006(device_path)
print(f"model:{device.type}")
print(f"fw:{device.fw}")
device.enable = False
print(f"output:{True if device.enable == 1 else False }")
