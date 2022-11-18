# rd60xx_gateway

RIDENの安定化電源 60xxシリーズをソケット通信で制御するためのゲートウェイ

# Requirements

- python 3.8
- pyserial
- minimalmodbus
- rd6006(https://github.com/Baldanos/rd6006/)

# Usage

```bash
./server.py "/dev/<serial_port>"
```
