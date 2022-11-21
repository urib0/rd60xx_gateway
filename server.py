#!/usr/bin/env python3

import socket
from rd6006 import RD6006
import json
import pprint

# 設定値読み込み
with open("./config.json", "r") as f:
    conf = json.loads(f.read())

device_path = conf["serialDevice"]
ip = conf["ipAddress"]
port = int(conf["port"])

# rd60xxと疎通確認
device = RD6006(device_path)
print(f"model:{device.type}")
print(f"fw:{device.fw}")
device.enable = False
print(f"output:{True if device.enable == 1 else False }")

# ソケット作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip,port))
sock.listen(1)
print(f"IPAddress:{ip}\nPORT:{port}")

while True:
    # ソケット接続待ち
    print("waiting for a connection...")
    client, remoteAddress = sock.accept()
    print(f"clientIPAddress:{remoteAddress}")

    while True:
        rcv_data = client.recv(1024).decode()

        if rcv_data:
            try:
                json_data = json.loads(rcv_data)
                pprint.pprint(json_data)
                client.sendall("200".encode())
            except Exception as e:
                print(rcv_data)
                client.sendall("400".encode())
                print(e)

        else:
            break
    client.close()
