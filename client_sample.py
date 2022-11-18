#!/usr/bin/env python3
import socket
import json
import time

# 設定値読み込み
with open("./config.json", "r") as f:
    conf = json.loads(f.read())

ip = conf["ipAddress"]
port = int(conf["port"])

# ソケット作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip,port))

sock.send("hoge".encode())
sock.send("piyo".encode())
sock.send("fuga".encode())

sock.close()