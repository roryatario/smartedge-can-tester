import random
import time

import can

from modbuscrc import crc

bus = can.interface.Bus(channel = 'can0', bustype='socketcan')

counter = 0

while True:
    data = counter.to_bytes(4, 'little')  + b'\x00\x00'
    crcval = crc(data)
    msg = can.Message(arbitration_id=counter,
                      data = crcval.to_bytes(2, 'little') + data,
                      extended_id=False)
    bus.send(msg)
    counter = (counter + 1) % (2**12)
    time.sleep(0.001)
