#!/usr/bin/env python3
import socket
import json
import time
import sys

# 設定値読み込み
with open("./config.json", "r") as f:
    conf = json.loads(f.read())

args = sys.argv
if len(args) == 2:
    msg = args[1].encode()
else:
    msg = '{\
        "hoge":1,\
        "piyo":2\
    }'.encode()

ip = conf["ipAddress"]
port = int(conf["port"])

# ソケット作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip,port))

sock.send(msg)
print(sock.recv(1024).decode())
sock.close()